from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleCommentFormView, ArticleFormCreateView, \
    ArticleFormEditView

urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path('<int:id>/', ArticleView.as_view()),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentFormView.as_view(), name='comment_create'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
]
