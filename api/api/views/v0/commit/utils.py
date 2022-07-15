from api.models.repo import Repo
from api.serializers.commit import CommitSerializer
from django.http import JsonResponse
from api.views.shared.utils import build_commit_array_from_request


def get_commits(request):
    owner = str(request.GET.get("owner"))
    repo_name = str(request.GET.get("repo"))
    token = str(request.GET.get("token"))

    repo = Repo(owner=owner, name=repo_name)
    data = build_commit_array_from_request(repo, token)
    serializer = CommitSerializer(data, many=True)
    return JsonResponse({"data": serializer.data})
