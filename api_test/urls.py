from django.urls import path
# from .views import article_list, article_detail
from .views import ArticleAPIView,ArticleDetail
urlpatterns = [
    # path('api/', article_list),
    path('api/', ArticleAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/',ArticleDetail.as_view())
]
