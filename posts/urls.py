from django.urls import path
from .views import GeneratePostAPIView

urlpatterns = [
    path("generate/", GeneratePostAPIView.as_view()),
]
