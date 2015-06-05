SRC_DIR = wafw00f
DOC_DIR = docs
MAKE = make

all:
	make install
	make test
	make html
	make clean

install:
	pip install -q -e .[dev,test,docs]

lint:
	prospector $(SRC_DIR) --strictness veryhigh

test:
	nosetests -c nose.cfg

testall:
	tox

html:
	cd $(DOC_DIR) && $(MAKE) html

htmlci:
	curl -X POST http://readthedocs.org/build/wafw00f

clean:
	rm -rf *.egg-info build dist .coverage
	find $(SRC_DIR) -name "*.pyc" | xargs rm -rf
