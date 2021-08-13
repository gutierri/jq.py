PREFIX	= /usr/local

BINDIR	= $(DESTDIR)$(PREFIX)/bin

INSTALL_PROGRAM = install -D

PROG=jq.py

.PHONY: all
all: test lint

.PHONY: test
test:
	@python3 -m unittest discover

.PHONY: lint
lint:
	@python3 -m pylint $(PROG)

.PHONY: install
install:
	$(INSTALL_PROGRAM) $(PROG) $(BINDIR)/$(PROG)
