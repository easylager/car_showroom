from config.celery import app
from celery.task import periodic_task
from celery.schedules import crontab


'''@periodic_task(run_every=(crontab(minute=('*/1'))), name='my_task')
def my_task():
    print(
        'my task'
    )
'''