from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
import datetime

#initializing 'app' and 'scheduler'
app = FastAPI()
scheduler = BackgroundScheduler()


#defining tasks
def task_1():
    print("Task 1 is executed at:", datetime.datetime.now())

def task_2():
    print("Task 2 is executed at:", datetime.datetime.now())

def task_3():
    print("Task 3 is executed at:", datetime.datetime.now())

scheduler.start()
#scheduling tasksusing 'add_job'
scheduler.add_job(task_1, 'interval', seconds=10)
scheduler.add_job(task_2, 'cron', hour =8, minute=0)
scheduler.add_job(task_3, 'interval', seconds=20)

#Creating API End Points
@app.get("/start_scheduler")
def start_scheduler():
    scheduler.start()
    return {"mesaage": "Schedule started"}

@app.get("/stop_scheduler")
def stop_scheduler():
    scheduler.shutdown()
    return {"mesaage": "Schedule stopped"}

@app.get("/list_jobs")
def list_jobs():
    jobs = scheduler.get_jobs()
    return {"jobs": [job.id for job in jobs]}





