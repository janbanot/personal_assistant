# Assistant feature ideas
Assistant should be availiable through various interfaces.
The main one would be discord bot - a server with multiple channels for diffrent purposes.
Additionally it should be availiable through voice assistant - using watch/phone commands + shortcuts

## Basic functionalities
- conversation bot - chat like experience, ask about anything
    - enrich the anwers with google search - from default or executed on demand
        - brave https://brave.com/search/api/
        - duckduckgo
        - serp api
- long term memory - use information from the knowledge base and info about user to enrich prompts to make answers it more accurate
    - config file with the basic info about the user to give the context
    - feature to save info to long term memory
    - feature to retrieve info from long term memory
- useful functions (chat modes)
    - prompts that can be used in various situations eg. correct grammar, wording, translate into diffrent languages
    - prompts for creating code - https://qdrant.tech/documentation/tutorials/code-search/
- create a day summary based on the calendar events
- remind about diffrent things based on the created events
    - feature to create reminder - remind me about sending that email in 30 minutes
    - feature to create recurring reminders - remind me to stand up every 30 minutes
- save notes/quotes from books, articles, etc.
    - save notes using chat or voice
        - save it with tags, so it can be easily categorized and then retrieved
    - daily summary (readwise like) - send a selected quote or note from the list and present it in the chat
    - feature to retrieve notes using tags

### Feature ideas for the future
- basic app instead of discord server - streamlit app?
- mode for creative ideas discussion, brainstorming, problem solving - agent like?
- help creating notes on content consumed (books, articles, videos, podcasts, films, series etc.)
    - summarize yt video
        - notes from dc:
        ```
        - data api + langchain package to scrape the transcript
        - converting timestamps so that they can be attached to a link referring to a specific point in time
        - loads the transcript directly from youtube - even the native one is sufficient.

        These two packages:
            import { YoutubeTranscript } from 'youtube-transcript';
            import {google } from 'googleapis';
        They allow you to load the video information and the transcript. All you need to do is link them together.
        And the search is based on the video_id
        ```
    - summarize podcast or article