# To Do List/Backlog for the project
- [x] project structure and initial setup
- [x] dockerize the app
- [x] add db migrations mechanism
- [x] add unit tests
- [x] add token-based authentication (JWT)
- [x] add test user and login endpoint
- [x] add langchain
- [x] add qdrant
- [x] create conversation bot foundation
- [x] configure CI/CD - github actions
- [x] rethink whole CI/CD workflow once again!
- [x] add discord bot
- [x] add basic option to talk with bot using model
- [x] YT video summary in English
- [] longterm memory and personalization RAG
    - [] create tables for longterm memory in postgres
    - [] analyze if/how it should be indexed in the qdrant
    - [] add endpoint to retrieve from longterm memory
    - [] add endpoint to save info to longterm memory
    - [] analzyze a mapping, how can save to longterm memory can be triggered in conversation
    - [] use that in conversation bot
- [] add functionality to create bookmarks (yt-videos, articles, etc.)
- [] create a diffrent yt video endpoint - list all elements mentioned in the video with timestamps?
- [] google search endpoint
- [] try using qa lanhgchain rag
- [] test diffrent models
    - [] anthropic claude
    - [] anthropic haiku
    - [] gemini
    - [] groq

# Nice to have/do
- [] use just for request notes for testing purposes
- [] change used library from request to aiohttp to allows async requests
- [] add types to the project
- [x] add langsmith support
- [] try what can be achieved with gpt-4o
- [] check coderabbit
- [] check dify over langsmith
- [] play with agents like approach
- [] check cloudflare workers
- [] check test containers (https://testcontainers.com/, https://www.docker.com/blog/local-development-of-go-applications-with-testcontainers/)

# Bugs
- [] fix issue with first build on the server (if there are no changes to the .env the setup will not be run and the whole build will fail)
- [] check why bot cointainer starts automatically when the docker engine is started
