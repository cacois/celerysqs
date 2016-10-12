import os
from celery import Celery
import ConfigParser

config = ConfigParser.ConfigParser()
print(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'settings.cfg'))
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'settings.cfg'))
print(config.get('celery', 'broker'))

app = Celery('tasks', broker=config.get('celery', 'broker'))

@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)
