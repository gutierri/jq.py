VENV_NAME?=.venv
PYTHON=${VENV_NAME}/bin/python
PREFIX	= /usr/local

BINDIR	= $(DESTDIR)$(PREFIX)/bin

INSTALL_PROGRAM = install -D

PROG=jq.py

$(VENV_NAME)/bin/activate:
	test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install pylint coverage
	touch $(VENV_NAME)/bin/activate

.PHONY: prepare_venv
prepare_venv: $(VENV_NAME)/bin/activate

.PHONY: all
all: test coverage lint

.PHONY: test
test: prepare_venv
	@python3 -m coverage run -m unittest discover -v

.PHONY: coverage
coverage: prepare_venv
	@python3 -m coverage report -m

.PHONY: lint
lint: prepare_venv
	@python3 -m pylint $(PROG)

.PHONY: install
install:
	$(INSTALL_PROGRAM) $(PROG) $(BINDIR)/$(PROG)
