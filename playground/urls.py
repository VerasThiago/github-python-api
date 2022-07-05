from django.urls import path
from .views.commit import commit

urlpatterns = [path("commits/", commit.GetCommits)]
