# docker-demo
Playing around with docker and AWS

## TODO App
Super simple web app which creates and shows a TODO list.
It consists of two parts friender anf bender. Friender generates the web front end and bender handles the backend and databse.

Run `TODOApp/run_flask.sh` to start both programs.

## Docker
Usefull/dangerous commands:
* `docker system prune [--all]`removes containers and images not used.
* `docker_*.sh` creates and runs a docker container with the TODO app. 