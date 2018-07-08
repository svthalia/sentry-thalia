.PHONY: clean develop lint publish

develop:
	pip install "pip>=7"
	pip install -e .

lint:
	@echo "--> Linting python"
	flake8
	@echo ""

publish:
	python setup.py sdist bdist_wheel upload

clean:
	rm -rf *.egg-info src/*.egg-info
	rm -rf dist build
