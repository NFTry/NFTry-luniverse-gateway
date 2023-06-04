.ONESHELL:

.PHONY: clean install run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	virtualenv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt;

run:
	. venv/bin/activate; \
	python manage.py run

all: clean install run
