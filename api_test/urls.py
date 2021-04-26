from django.urls import path
# from .views import article_list, article_detail
from .views import GenericAPIView
# from .views import ArticleAPIView,ArticleDetail,GenericAPIView
urlpatterns = [
    # path('api/', article_list),
    # path('api/', ArticleAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail),
    # path('detail/<int:id>/',ArticleDetail.as_view()),
    path('gen/<int:id>/',GenericAPIView.as_view())
]
