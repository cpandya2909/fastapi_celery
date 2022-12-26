# fastapi_celery
Run fastapi and celery in conjuction to run a command provided by user

# Files

|File|Descriptions|
|---|---|
| api.py | FastAPI server code |
| worker.py | Celery worker code with tasks |

# Steps

1. Copy both files in a single folder
2. Start the redis server. Redis is used as broker and backend for celery worker. "docker run -d -p 6379:6379 redis:alpine"
3. Start celery worker. "celery -A worker worker --loglevel=INFO ". Here "worker" is the file name of the file which contains tasks info.
4. start the api server. "uvicorn api:app --reload". Here "api" is the file name and "app" is the FastApi object
5. This will start the celery and FastAPI

# Run 

1. Open "http://localhost:8000/docs"
2. Use "/run-command" to send the command to server. Like "pwd". In response we will get task_id. Use this to get the response for server in next API call.
3. Use "/taks/{task_id}" to get the task status.
