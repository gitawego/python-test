PROJECT = "python test"

.PHONY: install
install: ;
	pip install virtualenv
	virtualenv ./virtualenv

.PHONY: initenv
initenv: ;
	. ./virtualenv/Scripts/activate



