from rest_framework.views import APIView
from api.models.commit import Commit
from api.serializers.commit import CommitSerializer
from api.views.v0.commit.utils import get_commits


class CommitViewSet(APIView):
    queryset = Commit.objects.all()
    serializer_class = CommitSerializer

    def get(self, request):
        return get_commits(request)
