# Useful developmnet notes

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