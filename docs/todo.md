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
- [] add functionality to create bookmarks (yt-videos, articles, etc.)
- [] add integration with apple watch using shortcuts to hit endpoints
- [] google search endpoint
- [] test diffrent models
    - [] anthropic claude/haiku
    - [] groq

# Nice to have/do
- [] change used library from request to aiohttp to allows async requests to improve performance
- [] add types to the project
- [x] add langsmith support
- [] try what can be achieved with gpt-4o
- [] refactor the code to avoid duplicates
- [] play with agents approach
- [] check cloudflare workers
- [] check test containers (https://testcontainers.com/, https://www.docker.com/blog/local-development-of-go-applications-with-testcontainers/)
- [] check idea of obsidian vault as knwoledge base

# Bugs
- [] fix issue with api not working after some time, no request are being processed and bot is throwning an error about missing summary in response. Add handling for such error and try to fix that issue
- [] check why bot cointainer starts automatically when the docker engine is started
- [] no login attempt before /commands, so there is error in case of no valid token
