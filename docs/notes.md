# Useful developmnet notes
### TODO
change to use https://github.com/casey/just

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