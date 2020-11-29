from __future__ import absolute_import
from celery.schedules import crontab
from datetime import timedelta


CELERY_IMPORTS = ('app.tasks.my_tasks')
CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'my_task-celery': {
        'task': 'app.tasks.my_tasks.print_hello',
        'schedule': timedelta(seconds=1)
    }
}
