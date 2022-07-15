# GITHUB PYTHON API

## 3 VERSIONS

### V0

No cache, it takes 7 seconds to retrieve data every time

```
curl --location --request GET 'localhost:8000/api/v0/get_commits?owner=OWNERNAME&repo=REPO_NAME&token=TOKEN'
```

### V1

Simple cache, it stores the commits for 15 seconds

```
curl --location --request GET 'localhost:8000/api/v1/get_commits?owner=OWNERNAME&repo=REPO_NAME&token=TOKEN'
```

### V2

Smart cache, it returns the old cached data while updates asynchronously

```
curl --location --request GET 'localhost:8000/api/v1/get_commits?owner=OWNERNAME&repo=REPO_NAME&token=TOKEN'
```

## Running

```bash
docker-compose up
```
