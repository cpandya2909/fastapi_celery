from celery import Celery
import subprocess

# Initialize Celery
celery = Celery(broker='redis://localhost:6379', backend='redis://localhost:6379')

@celery.task
def run_command(command):
    # Run the command using subprocess
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    return {
        "stdout": result.stdout.decode(),
        "stderr": result.stderr.decode(),
        "returncode": result.returncode
    }
