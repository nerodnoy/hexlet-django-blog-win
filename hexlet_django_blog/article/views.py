from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import ArticleCommentForm

from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={
            'article': article,
        })


class ArticleCommentFormView(View):

    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)  # Получаем данные формы из запроса
        if form.is_valid():  # Проверяем данных формы на корректность
            form.save()  # Сохраняем форму

# Если хотим сделать проверку на спам:
#        if form.is_valid(): # Проверяем данных формы на корректность
#            comment = form.save(commit=False) # Получаем заполненную модель
#            # Дополнительно обрабатываем модель
#            comment.content = check_for_spam(form.data['content'])
#            comment.save()
