from flask import Flask
#import celery
#import celery.bin.celery

from app.controllers.celery import make_celery

import os
import sys


app = Flask(__name__, static_folder=os.path.join(os.getcwd(), "app", "static"))
app.config.from_object("config")

cel = make_celery(app)

#status = celery.bin.celery.CeleryCommand.commands['status']()
#status.app = status.get_app()

from app.controllers import routes
