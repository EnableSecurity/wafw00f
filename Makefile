SRC_DIR = wafw00f
DOC_DIR = docs
MAKE = make

all:
	make install
	make test
	make html
	make clean

install:
	pip install -q -e .[dev,docs]

lint:
	prospector $(SRC_DIR) --strictness veryhigh

testall:
	tox

html:
	cd $(DOC_DIR) && $(MAKE) html

clean:
	rm -rf *.egg-info build dist .coverage
	find $(SRC_DIR) -name "*.pyc" | xargs rm -rf
