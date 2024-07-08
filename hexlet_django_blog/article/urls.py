from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleCommentFormView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view()),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentFormView.as_view(), name='comment_create'),
]
