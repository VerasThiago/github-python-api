import requests
from playground.models.commit import Commit
from playground.models.repo import Repo
from playground.serializers import commit as srlz
from django.http import JsonResponse
from playground.errors.errors import handle_exception

import json


THRESH_HOLD_SECONDS = 1 * 12


def getGithubUrl(repo):
    url = f"https://api.github.com/repos/{repo.owner}/{repo.name}/commits"
    return url


def getGithubHeaders(token):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Token {token}",
    }
    return headers


def parseCommitDataFromRequestToModel(commit):
    commit = Commit(
        author=commit["commit"]["author"]["name"],
        email=commit["commit"]["author"]["email"],
        date=commit["commit"]["author"]["date"],
        message=commit["commit"]["message"],
        sha=commit["commit"]["tree"]["sha"],
        url=commit["html_url"],
        comment_count=int(commit["commit"]["comment_count"]),
    )
    return commit


def parseCommitListDataFromRequestToModel(commitList):
    commitArray = []
    for commitRequest in commitList:
        commitModel = parseCommitDataFromRequestToModel(commitRequest)
        commitArray.append(commitModel)

    return commitArray


def buildCommitArrayFromRequest(repo, token):
    url = getGithubUrl(repo)
    headers = getGithubHeaders(token)

    resp = requests.request("GET", url, headers=headers)
    if resp.status_code != 200:
        raise Exception(resp.json(), resp.status_code)

    commits = parseCommitListDataFromRequestToModel(resp.json())
    return commits


def buildCommitArrayFromDB(repo):
    commits = Commit.objects.filter(repo__name__contains=repo.name)
    return commits


def isCached(repo):
    repos = Repo.objects.filter(name=repo.name, owner=repo.owner)
    if repos.count() == 0:
        return False, repo

    diff = repos.first().get_time_diff()
    return diff <= THRESH_HOLD_SECONDS, repos.first()


def JSONRsponseWithCache(cache, repo, data):
    if not cache:
        cacheData(repo, data)

    serializer = srlz.CommitSerializer(data, many=True)
    return JsonResponse({"cached": cache, "data": serializer.data})


def cacheData(repo, data):
    repo.save()

    for commit in data:
        try:
            Commit.objects.get(sha=commit.sha)
        except Commit.DoesNotExist:
            commit.repo = repo
            commit.save()


def get_commits(request):
    owner = str(request.GET.get("owner"))
    repo_name = str(request.GET.get("repo"))
    token = str(request.GET.get("token"))

    repo = Repo(owner=owner, name=repo_name)
    cached, repo = isCached(repo)
    if cached:
        data = buildCommitArrayFromDB(repo)
        return JSONRsponseWithCache(cache=True, repo=repo, data=data)

    try:
        data = buildCommitArrayFromRequest(repo, token)
        return JSONRsponseWithCache(cache=False, repo=repo, data=data)
    except Exception as e:
        return handle_exception(e)
