from django.urls import path, include

urlpatterns = [
    path("api/posts/", include("posts.urls")),
]
