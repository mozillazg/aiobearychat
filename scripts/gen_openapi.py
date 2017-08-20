# -*- coding: utf-8 -*-
import io
from collections import defaultdict
import datetime
import json
import os
import sys

import autopep8
import attr
import docformatter
from jinja2 import Environment, FileSystemLoader
from marshmallow import Schema, fields, post_load
import pypandoc

# TODO: 整理代码


def format_code(code_string):
    """调整代码格式,使之符合 PEP 8 和 PEP 257 规范"""
    pep8_code = autopep8.fix_code(code_string)
    doc_code = docformatter.format_code(pep8_code)
    return doc_code


@attr.s
class SwaggerMeta(object):
    host = attr.ib()
    basePath = attr.ib()
    schemes = attr.ib()
    produces = attr.ib()
    paths = attr.ib()


class SwaggerMetaSchema(Schema):
    host = fields.Str()
    basePath = fields.Str()
    schemes = fields.List(fields.Str())
    produces = fields.List(fields.Str())
    paths = fields.Dict()

    @post_load
    def make_object(self, data):
        return SwaggerMeta(**data)


@attr.s
class Parameter(object):
    name = attr.ib()
    in_ = attr.ib(default='query')
    description = attr.ib(default='')
    example = attr.ib(default='')
    required = attr.ib(default=False)
    type_ = attr.ib(default='string')
    default_ = attr.ib(default='')

    @property
    def type(self):
        return parameter_type_to_py(self.type_)

    @property
    def default(self):
        try:
            return json.loads(self.default_)
        except (ValueError, TypeError):
            return self.default_ or 'NOTHING'


class ParameterSchema(Schema):
    name = fields.Str()
    in_ = fields.Str(default='', load_from='in')
    description = fields.Str(default='')
    example = fields.Str(default='')
    required = fields.Boolean()
    type_ = fields.Str(default='string', load_from='type')
    default_ = fields.Raw(default='', load_from='default')

    @post_load
    def make_object(self, data):
        return Parameter(**data)


@attr.s
class APIDetail(object):
    uri = attr.ib(default='')
    method = attr.ib(default='get')
    content_type = attr.ib(default='application/json')
    description = attr.ib(default='')
    authentication = attr.ib(default=True)
    responses = attr.ib(default=attr.Factory(list))
    parameters = attr.ib(default=attr.Factory(list))  # type: list[Parameter]


class APIDetailSchema(Schema):
    uri = fields.Str(default='')
    content_type = fields.Str(default='application/json')
    method = fields.Str(default='get')
    description = fields.Str()
    authentication = fields.Boolean()
    responses = fields.Dict()
    parameters = fields.Nested(ParameterSchema, many=True, default=list)

    @post_load
    def make_object(self, data):
        data['responses'] = {
            k: ResponseSchema().load(v).data
            for k, v in data['responses'].items()
            if k != 'default'
            }
        return APIDetail(**data)


@attr.s
class Response(object):
    description = attr.ib(default='')
    examples = attr.ib(default=attr.Factory(dict))

    def example_d_with_pprint(self, n=8) -> dict:
        return {
            k: add_space_for_lines(v, n)
            for k, v in self.examples.items()
            }

    def first_example_with_pprint(self, n=8) -> str:
        d = self.example_d_with_pprint(n=n)
        if not d:
            return ''

        return list(d.values())[0]



class ResponseSchema(Schema):
    description = fields.Str()
    examples = fields.Dict()

    @post_load
    def make_object(self, data):
        return Response(**data)


_type_map = {
    'string': str,
    'boolean': bool,
    'array': list,
}


def parameter_type_to_py(type_):
    return _type_map[type_]


@attr.s
class API(object):
    kind = attr.ib(default='')
    uri = attr.ib(default='')
    content_type = attr.ib(default='application/json')
    authentication = attr.ib(default=True)
    http_method = attr.ib(default='get')
    func_name = attr.ib(default='')
    description = attr.ib(default='')
    params = attr.ib(default=attr.Factory(list))
    required_params = attr.ib(default=attr.Factory(list))
    optional_params = attr.ib(default=attr.Factory(list))
    # query_params = attr.ib(default=attr.Factory(list))
    # body_params = attr.ib(default=attr.Factory(list))
    responses = attr.ib(default=attr.Factory(dict))

    @classmethod
    def load_from_api_sepc(cls, api_spec):
        api = api_spec  # type: APIDetail
        uri = api.uri
        kind, func_name = cls.parse_api_name(uri)
        func_name = func_name or api.method
        required_params = []
        optional_params = []
        for param in api.parameters:
            param.description = md2rst(param.description.strip()).strip()
            if param.required:
                required_params.append(param)
            else:
                optional_params.append(param)

        description = md2rst(api.description.strip()).strip()
        responses = api.responses
        return cls(
            kind=kind,
            uri=uri,
            content_type=api.content_type,
            authentication=api.authentication,
            http_method=api.method,
            func_name=func_name,
            description=description,
            params=api.parameters,
            required_params=required_params,
            optional_params=optional_params,
            responses=responses,
        )

    @staticmethod
    def parse_api_name(uri):
        name = uri.strip('/').split('/')[-1]
        names = name.split('.')
        if len(names) > 1:
            return names[0], names[-1]
        else:
            return names[0], ''


def gen_cls_name(name):
    name = name.lower().replace('-', '_').replace('.', '_').strip('-')

    def upper_first(word):
        if len(word) > 1:
            return word[0].upper() + word[1:]
        else:
            return word.upper()

    words = name.split('_')
    return ''.join(map(upper_first, words))


def add_space_for_lines(text, n):
    lines = text.split('\n')
    s = []
    for line in lines:
        s.append(' ' * n + line)
    return '\n'.join(s)


def md2rst(text):
    return pypandoc.convert_text(text, 'rst', format='markdown_github')


with open(sys.argv[1]) as fp:
    swagger_json = fp.read()
    swagger_d = json.loads(swagger_json)

meta = SwaggerMetaSchema()
result = meta.load(swagger_d)
# print(result.data)
paths = result.data.paths
content_type = result.data.produces[0]
apis = {}

for key in paths.keys():
    api_d = paths[key]
    method = list(api_d.keys())[0]
    api = list(api_d.values())[0]
    sc = APIDetailSchema()
    result = sc.load(api)
    api_final = result.data
    api_final.method = method
    api_final.uri = key
    api_final.content_type = content_type

    apis[key] = api_final

current_dir = os.path.dirname(os.path.realpath(__file__))

template_env = Environment(
    autoescape=False, loader=FileSystemLoader(current_dir)
)  # type: Environment
template_env.globals.update({
    'len': len,
    'md2rst': md2rst,
})

template_one_api = template_env.get_template('openapi_one_api.py.jinja2')
template_merge_apis = template_env.get_template('openapi_merge_apis.py.jinja2')
template_doc = template_env.get_template('openapi.rst.jinja2')
os.environ.setdefault('PYPANDOC_PANDOC', '/usr/local/bin/pandoc')

api_group = defaultdict(list)

for uri, spec in apis.items():
    api = API.load_from_api_sepc(spec)
    api_group[api.kind].append(api)

api_modules = []
api_dir = sys.argv[2]
doc_dir = sys.argv[3]
now = datetime.datetime.now()
kind_docs = {
    'meta': 'meta 相关 API',
    'team': '团队相关 API',
    'user': '用户相关 API',
    'vchannel': '聊天会话相关 API',
    'channel': '讨论组相关 API',
    'session_channel': '临时讨论组相关 API',
    'p2p': 'P2P 会话相关 API',
    'message': '消息相关 API',
    'emoji': '团队自定义 emoji 相关 API',
    'sticker': '团队 sticker 相关 API',
    'rtm': 'RTM 相关 API',
}
base_url = 'https://api.bearychat.com/v1'


for kind, api_list in api_group.items():
    kind = kind.lower().replace('-', '_').replace('.', '_').strip('-')
    cls_name = '{0}API'.format(gen_cls_name(kind))
    module_name = '{0}_api'.format(kind)
    file_name = os.path.join(api_dir, '{0}.py'.format(module_name))
    kind_doc =  kind_docs.get(kind, '')
    api_modules.append({'kind': kind, 'kind_doc': kind_doc,
                        'cls_name': cls_name,
                        'module_name': module_name})
    print('generate {0}'.format(file_name))
    with io.open(file_name, 'w', encoding='utf-8') as fp:
        code = template_one_api.render(cls_name=cls_name, api_list=api_list,
                                       now=now, base_url=base_url,
                                       cls_doc=kind_doc).strip()
        formatted_code = format_code(code)
        fp.write(formatted_code)

print(api_modules)

file_name = os.path.join(api_dir, 'core.py')

print('generate {0}'.format(file_name))
with io.open(file_name, 'w', encoding='utf-8') as fp:
    code = template_merge_apis.render(
        api_modules=api_modules, now=now, base_url=base_url
    ).strip()
    formatted_code = format_code(code)
    fp.write(formatted_code)

file_name = os.path.join(doc_dir, 'openapi.rst')
print('generate {0}'.format(file_name))
with io.open(file_name, 'w', encoding='utf-8') as fp:
    doc = template_doc.render(
        api_modules=api_modules, now=now, base_url=base_url
    )
    fp.write(doc)
