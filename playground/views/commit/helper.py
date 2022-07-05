from unicodedata import name
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from ...models.commit import Commit
from ...models.repo import Repo


def buildCommitArrayFromRequest(repo, token):

    url = f"https://api.github.com/repos/{repo.owner}/{repo.name}/commits"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Token {token}",
    }
    commitList = requests.request("GET", url, headers=headers).json()

    commitArray = []

    repo.save()

    for commit in commitList:
        tmp = Commit(
            repo=repo,
            author=commit["commit"]["author"]["name"],
            email=commit["commit"]["author"]["email"],
            date=commit["commit"]["author"]["date"],
            message=commit["commit"]["message"],
            sha=commit["commit"]["tree"]["sha"],
            url=commit["html_url"],
            comment_count=int(commit["commit"]["comment_count"]),
        )
        tmp.save()

        tmp.cached = False
        commitArray.append(tmp.toJSON())

    return commitArray


def buildCommitArrayFromDB(repo):
    commitArray = []
    commitList = Commit.objects.filter(repo__name__contains=repo.name)

    for commit in commitList:
        commitArray.append(commit.toJSON())

    return commitArray


def isCached(repo):
    repos = Repo.objects.filter(name=repo.name, owner=repo.owner)
    return repos.count() > 0


def getCommits(owner, repo_name, token):
    repo = Repo(owner=owner, name=repo_name)

    if isCached(repo):
        return buildCommitArrayFromDB(repo)

    return buildCommitArrayFromRequest(repo, token)
