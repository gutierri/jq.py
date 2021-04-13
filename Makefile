PREFIX	= /usr/local
BINDIR	= $(DESTDIR)$(PREFIX)/bin

INSTALL_PROGRAM = install -D

PROG=jq.py

.PHONY: all
all: test lint

.PHONY: test
test:
	@python3 -m doctest -v $(PROG)

.PHONY: lint
lint:
	@pylint3 jq.py

.PHONY: install
install:
	$(INSTALL_PROGRAM) $(PROG) $(BINDIR)/$(PROG)
