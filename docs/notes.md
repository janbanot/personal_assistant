# Useful developmnet notes
### TODO
change to use https://github.com/casey/just
change to use password as variable that is set in the first command and then used in the next ones

## CURLs
- login
```bash
curl -X POST -H "Content-Type: application/json" -d '{"email": "test@test.com", "password": "test1"}' http://localhost:8081/login
```

- endpoint with token
```bash
curl -X GET -H "Authorization: Bearer ABC" http://localhost:8081/
```

- chat
```bash
curl -X POST -H "Authorization: Bearer ABC" -H "Content-Type: application/json" -d '{"message": "Hello"}' http://localhost:8081/chat
```

- save token as variable and use it later
```bash
TOKEN=$(curl -s -X POST -H "Content-Type: application/json" -d '{"email": "test@test.com", "password": "test1"}' http://localhost:8081/login | jq -r '.access_token')

curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"message": "Hello"}' http://localhost:8081/chat
```

- yt_summary endpoint
```bash
curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"url": "https://www.youtube.com/watch?v=YEJUUB1LNFM"}' http://localhost:8081/yt-summary
```

- check_english endpoint
```bash
curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"text": "My name is Susan. Im fourteen and I live in Germany. My hobbies are going to discos, sometimes I listen to music on the radio. In the summer, I go swimming in a lake. I dont have any brothers or sisters. We take buses to school. Im in year 9 at my school. My birthday is on Friday. I hope I will get a new guitar."}' http://localhost:8081/check-english
```

- debug in docker contianer
    - add debugpy fragment to the code
    ``` python
    import debugpy
    debugpy.listen(("0.0.0.0", 5678))
    debugpy.wait_for_client()
    ```
    - in docker-compose expose port 5678
    ```yaml
    services:
        your-service:
            ports:
                - "5678:5678"
    ```
    - modify lanuch.json config
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Remote Attach",
                "type": "python",
                "request": "attach",
                "connect": {
                    "host": "localhost",
                    "port": 5678
                },
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "/app"
                    }
                ]
            }
        ]
    }
    ```
    - add breakpoint in the code
    ```python
    debugpy.breakpoint()
    ```
    - run docker-compose
    - attach debugger in VSCode