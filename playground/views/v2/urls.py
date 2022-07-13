from django.urls import path
from playground.views.v2.commit import commit

urlpatterns = [
    path("get_commits/", commit.CommitViewSet.as_view()),
]
