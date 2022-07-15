from django.db import models
from .repo import Repo


class Commit(models.Model):
    repo = models.ForeignKey(Repo, on_delete=models.CASCADE)

    sha = models.CharField(max_length=128)
    author = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeField()
    message = models.TextField()
    url = models.URLField(max_length=128)
    comment_count = models.IntegerField()

    def __str__(self) -> str:
        return self.sha
