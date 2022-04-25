.PHONY: init 

init: down up ps com
down:
	docker-compose down --volumes --remove-orphans
pull:
	docker-compose pull
build:
	docker-compose build
up: pull build
	docker-compose up -d
ps:
	docker-compose ps
com:
	 docker-compose run --rm core python trans.py
