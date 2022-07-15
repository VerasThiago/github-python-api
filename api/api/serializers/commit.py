from rest_framework import serializers
from api.models.commit import Commit


class CommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commit
        fields = "__all__"
