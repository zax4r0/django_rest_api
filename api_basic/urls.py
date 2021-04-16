from django.urls import path
from .views import article_list, article_detail

urlpatterns = [
    path('api/', article_list),
    path('detail/<int:pk>/', article_detail),
]
