from django.db import models
from django.utils.timezone import utc
from datetime import datetime


class Repo(models.Model):
    owner = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def get_time_diff(self):
        if self.updated_at:
            now = datetime.utcnow().replace(tzinfo=utc)
            timediff = now - self.updated_at
            return timediff.total_seconds()

    class Meta:
        db_table = "api_repo"
