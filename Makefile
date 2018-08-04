define HELP_MESSAGE
Usage: make [COMMAND]

Commands:
	install     Install the dependencies.
	serve       Run django server.
	test        Run the tests and exit.
	help        Display this help message.
endef


export HELP_MESSAGE

.PHONY: serve install test help


install:

	pipenv install --three


serve:

	python manage.py runserver


test:

	@echo "all-good"


help:

	@echo "$$HELP_MESSAGE"
