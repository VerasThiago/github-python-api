from api.models.commit import Commit
from time import sleep
import requests

CACHE_THRESH_HOLD_SECONDS = 1 * 15
FAKE_DELAY_TIME = 7


def fake_github_deplay_time():
    sleep(FAKE_DELAY_TIME)


def get_github_api_url(repo):
    url = f"https://api.github.com/repos/{repo.owner}/{repo.name}/commits"
    return url


def get_github_api_headers(token):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Token {token}",
    }
    return headers


def parse_commit_from_git_to_commit_model(commit):
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


def parse_commit_list_from_git_to_commit_model_list(commitList):
    commitArray = []
    for commitRequest in commitList:
        commitModel = parse_commit_from_git_to_commit_model(commitRequest)
        commitArray.append(commitModel)

    return commitArray


def build_commit_array_from_request(repo, token):
    # Just to simulate long github request
    fake_github_deplay_time()

    url = get_github_api_url(repo)
    headers = get_github_api_headers(token)
    resp = requests.request("GET", url, headers=headers)
    commits = parse_commit_list_from_git_to_commit_model_list(resp.json())
    return commits


def build_commit_array_from_db(repo):
    commits = Commit.objects.filter(repo__name__contains=repo.name)
    return commits
