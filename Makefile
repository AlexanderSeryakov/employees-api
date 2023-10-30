DC = docker compose
BACKEND_DEV = docker-compose-dev.yaml

up-server:
	${DC} -f ${BACKEND_DEV} up --remove-orphans -d --build
down-server:
	${DC} -f ${BACKEND_DEV} down