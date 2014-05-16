SRC_DIR = wafw00f
DOC_DIR = docs
MAKE = make

all:
	make installall
	make lint
	make test
	make html
	make clean

install:
	pip install -r requirements.txt

installall:
	pip install -r requirements/prod.txt
	pip install -r requirements/dev.txt
	pip install -r requirements/docs.txt
	pip install -r requirements/test.txt

lint:
	pylint --rcfile=.pylintrc -E $(SRC_DIR)

lintall:
	pylint --rcfile=.pylintrc $(SRC_DIR)

test:
	nosetests -c nose.cfg

testall:
	tox

html:
	cd $(DOC_DIR) && $(MAKE) html

htmlci:
	curl -X POST http://readthedocs.org/build/wafw00f

clean:
	rm -rf *.egg-info
	rm -rf build/*
	rm -rf dist/*
	rm -rf $(SRC_DIR)/*.egg-info
	find $(SRC_DIR) -name "*.pyc" | xargs rm
