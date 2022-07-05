from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from .helper import getCommits


def GetCommits(request: WSGIRequest):
    owner = str(request.GET.get("owner"))
    repo = str(request.GET.get("repo"))
    token = str(request.GET.get("token"))

    return HttpResponse(getCommits(owner, repo, token))
