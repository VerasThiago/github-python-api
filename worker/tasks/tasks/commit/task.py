from __future__ import absolute_import, unicode_literals

from worker.celery import app
from tasks.models.repo import Repo
from tasks.serializers.commit import CommitSerializer
from .utils import build_commit_array_from_git_request, save_commit_array_db


@app.task(name='github_api_request_and_save_db')
def github_api_request_and_save_db(repo_owner, repo_name, token):
    repo = Repo.objects.get(owner=repo_owner, name=repo_name)

    commit_array = build_commit_array_from_git_request(repo.owner, repo.name,
                                                       token)

    save_commit_array_db(commit_array, repo)

    commits_serialized = CommitSerializer(commit_array, many=True)
    return commits_serialized.data
