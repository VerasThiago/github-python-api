from django.urls import path
from api.views.v1.commit import commit

urlpatterns = [
    path("get_commits/", commit.CommitViewSet.as_view()),
]
