.PHONY: nop
nop:
	@echo Hello!


.PHONY: test-all
test-all:
	$(MAKE) test-integration


.PHONY: test-integration
test-integration:
	$(MAKE) -C containers up
	$(MAKE) test-integration-pytest


PYTEST := rye run pytest
PYTEST_FLAGS := -vv


.PHONY: test-integration-pytest
test-integration-pytest:
	$(PYTEST) $(PYTEST_FLAGS) tests/integration
