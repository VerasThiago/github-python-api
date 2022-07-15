from api.models.repo import Repo
from django.http import JsonResponse
from server.celery import app
from api.utils.cache_type import RepoCacheType
from api.views.shared.utils import CACHE_THRESH_HOLD_SECONDS, build_commit_array_from_db
from api.serializers.commit import CommitSerializer


def repo_cache_status(repo):
    repos = Repo.objects.filter(name=repo.name, owner=repo.owner)
    if repos.count() == 0:
        return RepoCacheType.NO_CACHE, repo

    repo = repos.first()
    cacheTime = repos.first().get_time_diff()
    if cacheTime <= CACHE_THRESH_HOLD_SECONDS:
        return RepoCacheType.CACHE_HIT, repo
    else:
        return RepoCacheType.CACHE_MISS, repo


def json_response_from_db(cache_type, repo):
    commits = build_commit_array_from_db(repo)
    serializer = CommitSerializer(commits, many=True)
    return JsonResponse(
        {
            "cache_status": cache_type.name,
            "data": serializer.data,
        }
    )


def get_commits(request):
    owner = str(request.GET.get("owner"))
    repo_name = str(request.GET.get("repo"))
    token = str(request.GET.get("token"))

    repo_cache_type, repo = repo_cache_status(
        Repo(owner=owner, name=repo_name))

    if repo_cache_type == RepoCacheType.CACHE_HIT:
        return json_response_from_db(repo_cache_type, repo)

    # Force next requets to not trigger celery task
    # This might have a small gap with false cached data but it's fine
    repo.save()
    task_result = app.signature(
        "github_api_request_and_save_db", args=(repo.owner, repo.name, token)
    ).delay()

    if repo_cache_type == RepoCacheType.CACHE_MISS:
        return json_response_from_db(repo_cache_type, repo)
    if repo_cache_type == RepoCacheType.NO_CACHE:
        return JsonResponse(
            {
                "cache_status": repo_cache_type.name,
                "id": task_result.id,
            }
        )
    return JsonResponse(
        {
            "cache_status": RepoCacheType.UNKNOWN,
            "id": task_result.id,
        }
    )
