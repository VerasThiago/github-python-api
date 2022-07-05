from django.contrib import admin
from .models.commit import Commit
from .models.repo import Repo

admin.site.register(Repo)
admin.site.register(Commit)
