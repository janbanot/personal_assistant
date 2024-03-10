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