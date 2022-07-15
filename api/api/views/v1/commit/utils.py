from api.models.commit import Commit
from api.models.repo import Repo
from api.serializers.commit import CommitSerializer
from django.http import JsonResponse

from api.views.shared.utils import CACHE_THRESH_HOLD_SECONDS, build_commit_array_from_db, build_commit_array_from_request


def is_cached(repo):
    repos = Repo.objects.filter(name=repo.name, owner=repo.owner)
    if repos.count() == 0:
        return False, repo

    diff = repos.first().get_time_diff()
    return diff <= CACHE_THRESH_HOLD_SECONDS, repos.first()


def json_response_with_cache(cache, repo, data):
    if not cache:
        cache_data(repo, data)

    serializer = CommitSerializer(data, many=True)
    return JsonResponse({"cached": cache, "data": serializer.data})


def cache_data(repo, data):
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
    cached, repo = is_cached(repo)
    if cached:
        data = build_commit_array_from_db(repo)
        return json_response_with_cache(cache=True, repo=repo, data=data)

    data = build_commit_array_from_request(repo, token)
    return json_response_with_cache(cache=False, repo=repo, data=data)
