from rest_framework import serializers
from api.models.repo import Repo


class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repo
        fields = "__all__"
