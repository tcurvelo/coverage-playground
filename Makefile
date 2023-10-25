RUN ?= python -m

.PHONY: server tests coverage

server:
	@echo "Starting server..."
	$(RUN) uvicorn todate.api:app

server-w-cov:
	$(MAKE) server COVERAGE_FILE=.coverage_server RUN="coverage run --source=todate -m"

tests:
	COVERAGE_FILE=.coverage_client coverage run --source=todate -m pytest .


coverage:
	coverage combine .coverage*
	coverage report