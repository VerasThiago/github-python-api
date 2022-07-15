from rest_framework.views import APIView
from api.models.commit import Commit
from api.serializers import commit as srlz
from api.views.v2.commit.utils import get_commits


class CommitViewSet(APIView):
    queryset = Commit.objects.all()
    serializer_class = srlz.CommitSerializer

    def get(self, request):
        return get_commits(request)
