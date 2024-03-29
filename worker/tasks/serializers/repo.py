from rest_framework import serializers
from tasks.models.repo import Repo


class RepoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repo
        fields = "__all__"
