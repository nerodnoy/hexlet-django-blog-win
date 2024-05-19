from django.shortcuts import render


def index(request, tags, article_id):
    return render(request, 'articles/index.html',
                  context={
                      'tags': tags,
                      'article_id': article_id,
                  })
