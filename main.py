from sqlalchemy_scheduler_models import DatabaseSchedulerEntry, CrontabSchedule, Base, engine
from sqlalchemy_scheduler import dbsession

# create all tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

## Adds a scheduled task for function: add(3,6)
dse = DatabaseSchedulerEntry()
dse.name = 'Simple add task'
dse.task = 'celerysqs.tasks.add'
dse.arguments = '[7,2]'  # json string
dse.keyword_arguments = '{}'  # json string

# crontab defaults to run every minute
dse.crontab = CrontabSchedule()
dbsession.add(dse)

dbsession.commit()
