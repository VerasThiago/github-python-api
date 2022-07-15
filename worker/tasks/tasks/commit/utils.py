import requests
from time import sleep
from tasks.models.commit import Commit


def get_github_api_url(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
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


def save_commit_array_db(commit_array, repo):
    for commit in commit_array:
        commit.repo = repo
        try:
            Commit.objects.get(sha=commit.sha)
        except Commit.DoesNotExist:
            commit.repo = repo
            commit.save()


def build_commit_array_from_git_request(repo_owner, repo_name, token):
    # Just to simulate long github request
    sleep(15)

    url = get_github_api_url(repo_owner, repo_name)
    headers = get_github_api_headers(token)

    resp = requests.request("GET", url, headers=headers)

    commit_array = parse_commit_list_from_git_to_commit_model_list(resp.json())
    return commit_array