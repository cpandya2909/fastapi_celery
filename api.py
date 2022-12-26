from fastapi import FastAPI, HTTPException, Path
from celery import Celery
from celery.result import AsyncResult
from pydantic import BaseModel

app = FastAPI()

# Initialize Celery
celery = Celery(broker='redis://localhost:6379', backend='redis://localhost:6379')

# model to get command as POST input
class Command(BaseModel):
    command: str

@app.post("/run-command/")
async def run_command(command: Command):
    # Validate the input command
    if not command:
        raise HTTPException(status_code=400, detail="Command is required")
    print(command.command)
    # Run the command as a Celery task
    task = celery.send_task('tasks.run_command', args=[command.command])
    
    return {
        "task_id": task.id
    }

@app.get("/taks/{task_id}")
async def get_output(task_id: str = Path(title= "Task id")):
    # Validate the input command
    if not task_id:
        raise HTTPException(status_code=400, detail="Task id is required")

    task_info = AsyncResult(task_id)
    if task_info.ready():
        return{
            "data" : task_info.result
        }
    else:
        return{
            "data" : "Task is incomplete"
        }
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8899, workers=4)
