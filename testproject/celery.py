from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_study.settings")

app = Celery("celery_study")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks()
