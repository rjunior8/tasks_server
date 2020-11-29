from celery import Celery
import celeryconfig

from config import BROKER_URL


def make_celery(app):
    # create context tasks in celery
    celery = Celery(app.import_name, broker=BROKER_URL)
    celery.conf.update(app.config)
    celery.config_from_object(celeryconfig)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery

