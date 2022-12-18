up:
	docker-compose up

upd:
	docker-compose up -d

buildup:
	docker-compose up --build

buildupd:
	docker-compose up --build -d

migr:
	docker-compose exec back python manage.py makemigrations
	docker-compose exec back python manage.py migrate --noinput

migr-show:
	docker-compose exec back python manage.py showmigrations

migr-fake:
	docker-compose exec back python manage.py migrate --fake

static:
	docker-compose exec back python manage.py collectstatic --no-input --clear

admin:
	docker-compose exec back python manage.py createsuperuser

down:
	docker-compose down
	
downv:
	docker-compose down -v

tests:
	docker-compose exec back python manage.py test --verbosity 2

trans-prep:
	django-admin makemessages -l fr

translate:
	django-admin compilemessages

backup:
	./dump/dump_db.sh