.DEFAULT_GOAL := help
UWSGI_PID_FILE := var/uwsgi.pid
UWSGI_INI_FILE := conf/uwsgi.ini


.PHONY: env
env:
	@# Create virtual environment and Install tools.

	go get github.com/TakesxiSximada/unmake
	python3 -m venv .venv
	echo 'Please execute: source .venv/bin/activate'


.PHONY: develop
develop:
	@# Install dependencies for development.

	pip install -r requirements/develop.txt


.PHONY: requirements
requirements:
	@# Create requirements.txt

	pip-compile


.PHONY: deps
deps:
	@# Install dependencies for service.

	pip install -r requirements.txt


.PHONY: migrations
migrations:
	@# Create migration files.

	./manage.py web makemigrations


.PHONY: static
static:
	@# Create migration files.

	./manage.py web collectstatic


.PHONY: migrate
migrate:
	@# Execute migrations.

	./manage.py web migrate


.PHONY: superuser
superuser:
	@# Create administorator.

	./manage.py web createsuperuser


.PHONY: server
server:
	@# (Re)Start Web Server

	-make server-stop
	sleep 3
	uwsgi --ini $(UWSGI_INI_FILE) --pidfile $(UWSGI_PID_FILE)


.PHONY: server-reload
server-reload:
	@# Stop Web Server

	uwsgi --reload $(UWSGI_PID_FILE)


.PHONY: server-stop
server-stop:
	@# Stop Web Server

	uwsgi --stop $(UWSGI_PID_FILE)


.PHONY: help
help:
	@# Display help message

	@unmake $(MAKEFILE_LIST)
