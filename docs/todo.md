# To Do List/Backlog for the project
- [x] project structure and initial setup
    - [x] create simple flask api with first test endpoint
- [x] dockerize the app
    - [x] api/backend
    - [x] proxy
    - [x] db (postgres)
    - [x] docker-compose
- [x] add db migrations mechanism
- [x] add unit tests
- [x] add token-based authentication (JWT)
- [x] add test user and login endpoint
- [x] add langchain
- [x] add qdrant
- [x] create conversation bot foundation
- [x] configure CI/CD - github actions
    - [x] fix issue with missing .env file - use github secrets and crate step in workflow to create .env file
- [x] rethink whole CI/CD workflow once again!
    - [x] check what makes sense i.e. build, then reuse that for tests and if ok, don't build again
    - [x] check why changes in test were not taken into consideration!
- [x] add discord bot
    - [] figure out better use of discord slash commands
    - [] add clearing context automaticaly after some time
- [x] add basic option to talk with bot using model
- [x] YT video summary in English
- [] longterm memory and personalization RAG
    - [] create tables for longterm memory in postgres
    - [] analyze if/how it should be indexed in the qdrant
    - [] add endpoint to retrieve from longterm memory
    - [] add endpoint to save info to longterm memory
    - [] analzyze a mapping, how can save to longterm memory can be triggered in conversation
    - [] use that in conversation bot
- [] try using qa lanhchain rag
- [] test diffrent models
    - [] anthropic claude
    - [] anthropic haiku
    - [] gemini
    - [] groq

# Nice to have/do
- [] change used library from request to aiohttp to allows async requests
- [] add types to the project
- [] add langsmith support
- [] check coderabbit
- [] check cloudflare workers

# Bugs
- [] fix issue with first build on the server (if there are no changes to the .env the setup will not be run and the whole build will fail)
- [] check why postgres is not destroyed correctly after tests
- [] check why bot cointainer starts automatically when the docker engine is started
