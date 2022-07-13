from django.urls import path, include

urlpatterns = [
    path("v1/", include("playground.views.v1.urls")),
    path("v2/", include("playground.views.v2.urls")),
]
