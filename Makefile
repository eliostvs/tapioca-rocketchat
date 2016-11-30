.PHONY: clean-pyc clean-build docs clean test lint

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "test - run tests quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "dist - package"

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

test: clean
	python setup.py test

docs:
	rm -f docs/tapioca-rocketchat.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ tapioca-rocketchat
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

release.test: dist
	python setup.py register -r pypitest
	python setup.py sdist upload -r pypitest # --identity="Elio Esteves Duarte" --sign
	python setup.py bdist_wheel upload -r pypitest #--identity="Elio Esteves Duarte" --sign

release: dist
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi #--identity="Elio Esteves Duarte" --sign
	python setup.py bdist_wheel upload -r pypi #--identity="Elio Esteves Duarte" --sign

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist
