from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view()),
    # Для комментариев к статье
    # path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
]
