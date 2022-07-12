from django.urls import path, include
from playground.views.commit import commit
from rest_framework import routers
from playground.views.commit import commit

urlpatterns = [
    path("get_commits/", commit.CommitViewSet.as_view()),
]
