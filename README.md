# ODBot - Telegram Bot

ODBot is a Telegram bot designed to facilitate user interactions through commands. It allows users to manage a list of topics, control user access via a whitelist, and provides administrative commands for managing the bot.

## Features

- **Whitelist Management**: Restrict bot usage to users listed in a whitelist.
- **Topic Management**: Users can add, delete, and list topics.
- **Administrative Commands**: Special commands for bot administrators to manage the whitelist.
- **Logging**: Detailed logging of bot activities and user interactions.

## Commands

- `/start` or `/help`: Display a welcome message and list available commands.
- `/whitelist <username>`: Add a user to the whitelist (admin only).
- `/ban <username>`: Remove a user from the whitelist (admin only).
- `/show`: Show the list of whitelisted users (admin only).
- `/add <topic>`: Add a topic to the list.
- `/del <topic>` or `/del all`: Delete a topic from the list or all topics.
- `/list`: List all topics.

## Setup

1. Clone the repository to your local machine.
2. Create a `.env` file based on the `.env.sample` and fill in the required environment variables.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Make sure to create a `whitelist.txt` file in the `config` directory or adjust the `WHITELIST_FILE_PATH` in `config/settings.py`.

## Makefile Usage

The project includes a `Makefile` which provides convenient commands for setting up and managing the project:

- `make install`: Set up the project by creating a virtual environment and installing dependencies.
- `make run`: Run the bot using the virtual environment.
- `make clean`: Clean the project by removing the virtual environment and any compiled Python files.
- `make docker-build`: Build the Docker containers.
- `make docker-up`: Start the Docker containers in detached mode.
- `make docker-down`: Stop and remove the Docker containers.
- `make docker-restart`: Restart the Docker containers.
- `make docker-logs`: Show the logs of the odbot Docker container.
- `make docker-reset`: Reset the Docker containers by stopping them, pulling the latest changes, rebuilding the containers, and starting them again.
- `make reset`: Reset the project by cleaning, pulling the latest changes, installing dependencies, and resetting Docker containers.

To use these commands, simply run `make <command>` in your terminal.

## Docker Usage

To build and run the bot using Docker, execute the following commands:

```bash
make docker-build
make docker-up
```

This will build the Docker image and start the bot in a Docker container. To view the logs, use:

```bash
make docker-logs
```

To stop and remove the Docker containers, use:

```bash
make docker-down
```

## Administrative Commands

Some commands are restricted and can only be used by the admin user defined in the `BOT_ADMIN_USERNAME` environment variable. These commands include managing the whitelist and banning users.

## Logging

Logs are written to `logs/odbot.log` and to the console. The log level can be adjusted via the `LOG_LEVEL` environment variable.

## License

This project is licensed under the terms of the MIT license.
