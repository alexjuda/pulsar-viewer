.PHONY: nop
nop:
	@echo Hello!


.PHONY: test-all
test-all:
	$(MAKE) test-integration


PYTEST := rye run pytest
PYTEST_FLAGS := -vv


# Requires starting the Pulsar container first:
# make -C containers up
.PHONY: test-integration
test-integration:
	$(PYTEST) $(PYTEST_FLAGS) tests/integration
