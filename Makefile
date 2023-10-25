RUN ?= python -m

.PHONY: server tests cov coverage

server:
	$(RUN) uvicorn todate.api:app

cov:
	$(eval export RUN := coverage run -a -m)

tests:
	$(RUN) pytest .

report:
	coverage report

clean:
	rm .coverage