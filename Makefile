clear:
	pip uninstall delivery

install:
	pip install -e .['dev']

test:
	pytest ./tests -v --cov="delivery"