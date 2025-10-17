SHELL := /bin/bash
PIPENV := pipenv run

install:
	@pipenv install

train:
	@$(PIPENV) python run_matcher.py batch

api:
	@$(PIPENV) python api.py

cli:
	@$(PIPENV) python run_matcher.py

test:
	@$(PIPENV) python tests/test_data.py

batch:
	@$(PIPENV) python run_matcher.py batch

clean:
	@rm -rf __pycache__ data/processed/*.csv

lint:
	@$(PIPENV) flake8 models/ run_matcher.py api.py

notebook:
	@$(PIPENV) jupyter notebook
