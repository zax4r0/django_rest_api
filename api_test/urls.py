from django.urls import path
from .views import GenericAPIView

urlpatterns = [

    path('gen/article/detail/<int:id>/',GenericAPIView.as_view()),
    path('gen/article/detail/',GenericAPIView.as_view())
]
