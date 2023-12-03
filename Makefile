DOCKER_COMPOSE = docker-compose

reset: clean pull install docker-down docker-build docker-up

install: create-venv install-requirements

create-venv:
	python3 -m venv venv

install-requirements:
	. venv/bin/activate && \
	pip3 install --upgrade pip && \
	pip3 install -r requirements.txt

pull:
	git pull origin main

run:
	. venv/bin/activate && \
	python main.py

clean:
	deactivate || true
	rm -rf venv
	find . -name *.pyc -delete
	find . -name __pycache__ -delete

docker-build:
	$(DOCKER_COMPOSE) build

docker-up:
	$(DOCKER_COMPOSE) up -d

docker-down:
	$(DOCKER_COMPOSE) down

docker-restart: docker-down docker-up

docker-logs:
	$(DOCKER_COMPOSE) logs -f odbot

docker-reset: docker-down pull docker-build docker-up

help:
	@echo "\n\033[1mCode commands:\033[0m\n"
	@echo "  \033[1mclean:\033[0m Clean the project removing the venv directory, and deleting compiled Python files and cache."
	@echo "  \033[1mcreate-venv:\033[0m Create a Python virtual environment."
	@echo "  \033[1minstall-requirements:\033[0m Install project dependencies from requirements.txt file."
	@echo "  \033[1minstall:\033[0m Create a virtual environment and install project dependencies."
	@echo "  \033[1mpull:\033[0m Pull the latest changes from the main branch of the repository."
	@echo "  \033[1mreset:\033[0m Reset the project by cleaning, pulling latest changes, installing dependencies, and resetting Docker containers."
	@echo "  \033[1mrun:\033[0m Run the main.py script."
	@echo "\n\033[1mDocker commands:\033[0m\n"
	@echo "  \033[1mdocker-build:\033[0m Build Docker containers using docker-compose."
	@echo "  \033[1mdocker-down:\033[0m Stop and remove Docker containers using docker-compose."
	@echo "  \033[1mdocker-logs:\033[0m Show the logs of the odbot Docker container."
	@echo "  \033[1mdocker-reset:\033[0m Reset Docker containers by stopping and removing them, pulling latest changes, building containers, and starting them again."
	@echo "  \033[1mdocker-restart:\033[0m Restart Docker containers by stopping and removing them, and then starting them again."
	@echo "  \033[1mdocker-up:\033[0m Start Docker containers in detached mode using docker-compose."
	@echo "  \033[1mhelp:\033[0m Show this help\n"

