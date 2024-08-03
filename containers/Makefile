.PHONY: nop
nop:
	@echo Hello!


COMPOSE := podman compose


.PHONY: up
up:
	$(COMPOSE) up -d


.PHONY: down
down:
	$(COMPOSE) down --volumes --remove-orphans


.PHONY: redo
redo:
	$(MAKE) down
	$(MAKE) up
