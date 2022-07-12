from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from playground.views.commit.helper import isCached
from playground.models.commit import Commit
from playground.serializers import commit as srlz
from .helper import get_commits


class CommitViewSet(APIView):
    queryset = Commit.objects.all()
    serializer_class = srlz.CommitSerializer

    def get(self, request):
        return get_commits(request)
