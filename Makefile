clear:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
<<<<<<< HEAD
	@find ./delivery -name '__pycache__' -exec rm -rf {} \;
=======
>>>>>>> master
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip uninstall delivery

install:
	pip install -e .['dev'] --upgrade --no-cache

test:
	pytest ./tests -v --cov="delivery"

run:
	cd ./delivery/ && flask run