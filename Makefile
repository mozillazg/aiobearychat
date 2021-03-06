.PHONY: clean-pyc clean-build docs clean
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

OPENAPI_SPEC_JSON := "scripts/swagger.json"
OPENAPI_DIR := "aiobearychat/openapi/"
OPENAPI_DOC_DIR := "docs/api/"
PYPANDOC_PANDOC := "$(shell which pandoc)"

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "release-test - package and upload a release to test pypi server"
	@echo "dist - package"
	@echo "install - install the package to the active Python's site-packages"
	@echo "gen_openapi - generate open api code"
	@echo "down_openapi_spec - download open api sepc json file"

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint:
	flake8 aiobearychat tests

test:
	py.test --cov aiobearychat tests --cov-report=term-missing

test-all:
	tox

coverage: test
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs:
	rm -f docs/aiobearychat.rst
	rm -f docs/modules.rst
	# sphinx-apidoc -o docs/ aiobearychat
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	# $(BROWSER) docs/_build/html/index.html

release: clean
	python setup.py sdist upload
	python setup.py bdist_wheel upload

release-test: clean
	python setup.py sdist upload -r test
	python setup.py bdist_wheel upload -r test

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean
	pip install -r requirements_dev.txt
	python setup.py install

down_openapi_spec:
	-rm $(OPENAPI_SPEC_JSON)
	curl https://raw.githubusercontent.com/bearyinnovative/OpenAPI/master/api/swagger.json \
		 -o $(OPENAPI_SPEC_JSON)

gen_openapi: down_openapi_spec
	PYPANDOC_PANDOC=$(PYPANDOC_PANDOC) \
	python scripts/gen_openapi.py $(OPENAPI_SPEC_JSON) $(OPENAPI_DIR) $(OPENAPI_DOC_DIR)
