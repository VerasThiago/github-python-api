from rest_framework import serializers
from tasks.models.commit import Commit


class CommitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commit
        fields = "__all__"
