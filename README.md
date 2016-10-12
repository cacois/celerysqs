# celerysqs

Some example code using celery and celery beat with SQS as a broker and SQLAlchemy to store the task schedules

SQLAlchemy scheduler adapted from https://github.com/tuomur/celery_sqlalchemy_scheduler

## Step 1: Copy settings.cfg.example into settings.cfg

Note: all steps should be performed from _outside_ the celerysqs directory

    $ mv celerysqs/settings.cfg.example celerysqs/settings.cfg

Update this file to contain your aws_access_key_id and aws_secret_access_key.

## Step 2: Run main.py to insert schedules into the db

    $ python -m celerysqs.main

The example is currently configured to write to a local sqlite db file named app.db. This can be easily reconfigured to meet your needs. By default, we are inserting a single task to run the add() function every 60 seconds.

## Step 3: Run a worker

    $ celery -A celerysqs.tasks worker --loglevel=info

This worker will sit and wait for tasks to come onto the SQS queue, and will execute them when they appear.

## Step 4: Run the Scheduler

    $ celery -A celerysqs.tasks beat -S celerysqs.sqlalchemy_scheduler.DatabaseScheduler
