from dataclasses import fields
from rest_framework import serializers
from playground.models.commit import Commit


class CommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commit
        fields = "__all__"
