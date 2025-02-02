up:
	DOCKER_CLIENT_TIMEOUT=600 COMPOSE_HTTP_TIMEOUT=600 docker-compose up

upd:
	DOCKER_CLIENT_TIMEOUT=600 COMPOSE_HTTP_TIMEOUT=600 docker-compose up -d

buildup:
	DOCKER_CLIENT_TIMEOUT=600 COMPOSE_HTTP_TIMEOUT=600 docker-compose up --build

buildupd:
	DOCKER_CLIENT_TIMEOUT=600 COMPOSE_HTTP_TIMEOUT=600 docker-compose up --build -d

exec:
	docker-compose exec back ./manage.py $(filter-out $@,$(MAKECMDGOALS))

migr:
	docker-compose exec back ./manage.py makemigrations
	docker-compose exec back ./manage.py migrate --noinput

show:
	docker-compose exec back ./manage.py showmigrations

migr-fake:
	docker-compose exec back ./manage.py migrate --fake

static:
	docker-compose exec back ./manage.py collectstatic --no-input --clear

admin:
	docker-compose exec back ./manage.py createsuperuser

down:
	docker-compose down

downv:
	docker-compose down -v

tests:
	docker-compose exec back ./manage.py test --verbosity 2

trans-prep:
	django-admin makemessages -l fr

translate:
	django-admin compilemessages

backup:
	./dump/dump_db.sh

shell:
	docker-compose exec back ./manage.py shell_plus

load:
	docker-compose exec back ./manage.py loaddata user.json place_app.json membership.json

db:
	docker exec -it database psql --username=postgres --dbname=project_db

restart:
	docker-compose stop back && docker-compose up -d back

swagger:
	docker-compose exec back ./manage.py spectacular --color --file schema.yml
