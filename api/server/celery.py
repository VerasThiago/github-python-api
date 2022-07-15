from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

app = Celery("server")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks()
