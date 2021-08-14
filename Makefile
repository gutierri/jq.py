PREFIX	= /usr/local

BINDIR	= $(DESTDIR)$(PREFIX)/bin

INSTALL_PROGRAM = install -D

PROG=jq.py

.PHONY: all
all: test coverage lint

.PHONY: test
test:
	@python3 -m coverage run -m unittest discover -v

.PHONY: coverage
coverage:
	@python3 -m coverage report -m

.PHONY: lint
lint:
	@python3 -m pylint $(PROG)

.PHONY: install
install:
	$(INSTALL_PROGRAM) $(PROG) $(BINDIR)/$(PROG)
