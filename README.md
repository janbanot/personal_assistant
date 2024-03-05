# Personal Assistant
Introducing a virtual personal assistant for simplifying your daily tasks. Assistant will be accessible through Command Line Interface (CLI) or as a Discord bot. With help from GenerativeAI it will help you automate routine activities, making your life more efficient and organized.

Project built for the [100 commitów](https://100commitow.pl/) competition. Its goal is to develop an open source project for 100 days.

## Technologies
[![Technologies](https://skillicons.dev/icons?i=py,flask,postgres,docker)](https://skillicons.dev)

## How to run?
You only need to have docker and docker-compose installed on your machine. Then you can run the following commands:
1. ```git clone https://github.com/janbanot/personal_assistant.git``` - to clone the repository
2. ```bash env.sh``` - to create an image with python virtual environment and install all the dependencies
3. ```bash build.sh``` - to build the project
    - ```bash build.sh --local``` - to build the project using local docker-compose settings

## Read more
- [feature ideas](docs/feature_ideas.md)
- [todo list](docs/todo.md)
