from django.shortcuts import render


def index(request, tags, article_id):
    return render(request, 'article/index.html',
                  context={
                      'tags': tags,
                      'article_id': article_id,
                  })
