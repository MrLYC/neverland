requirements.txt:
	pip install -r requirements.txt

requirements-adv.txt:
	pip install -r requirements-adv.txt

.PHONY: migrate
migrate:
	python manage.py syncdb

.PHONY: create_admin
create_admin:
	python manage.py create_admin

.PHONY: git-update
git-update:
	git stash
	git pull --rebase origin
	git stash pop

.PHONY: update
update: git-update requirements.txt migrate
