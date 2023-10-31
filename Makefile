DC = docker compose
BACKEND_DEV = docker-compose-dev.yaml

runserver:
	${DC} -f ${BACKEND_DEV} up --remove-orphans -d --build
downserver:
	${DC} -f ${BACKEND_DEV} down
connect-mongo:
	${DC} -f ${BACKEND_DEV} exec mongodb sh
connect-app:
	${DC} -f ${BACKEND_DEV} exec application sh
