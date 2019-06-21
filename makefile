.PHONY: test lint run isort clean-pyc autopep8
HOST          = 127.0.0.1
TEST_PATH     = ./
VENV          = order
PROJECTS      = ./

help:
	@echo "    isort"
	@echo "        Sort import statements."
	@echo "    lint"
	@echo "        Check style with flake8."
	@echo "    test"
	@echo "        Run py.test"
	@echo "    run"
	@echo "        Run the my_project service on your local machine."

clean-pyc:
	find ./ -name "*.pyc" | xargs rm -rf

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

autopep8:
	autopep8  --in-place -r --aggressive ./*

lint:
	flake8 --exclude=.tox

test:
	nosetests -s -v --with-coverage --cover-package=$(TEST_PATH)

run:
	python app.py

