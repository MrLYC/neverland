PYTHON=python2

requirements.txt:
	pip install -r requirements.txt

requirements-adv.txt:
	pip install -r requirements-adv.txt

.PHONY: migrate
migrate:
	${PYTHON} manage.py syncdb

.PHONY: create_admin
create_admin:
	${PYTHON} manage.py create_admin

.PHONY: git-update
git-update:
	$(eval modified_files ?= $(shell git ls-files -m))
	[ "${modified_files}" != "" ] && git stash || true
	git pull --rebase origin || true
	[ "${modified_files}" != "" ] && git stash pop || true

.PHONY: update
update: git-update requirements.txt migrate
