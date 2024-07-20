import requests
from flask import Flask
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import os

app = Flask(__name__)

BASE_URL = os.environ.get("BASE_URL")


def print_date_time():
    r = requests.get(f"{BASE_URL}/health")
    print(r.text)


scheduler = BackgroundScheduler()
scheduler.add_job(func=print_date_time, trigger="interval", seconds=180)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


@app.route("/")
def hello():
    print("[bot] - hit base url")
    return "Hello, World!"


@app.route("/health")
def health():
    print("[bot] - hit health url")
    return "ok"
