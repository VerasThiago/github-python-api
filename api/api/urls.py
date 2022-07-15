from django.urls import path, include

urlpatterns = [
    path("v1/", include("api.views.v1.urls")),
    path("v2/", include("api.views.v2.urls")),
]
