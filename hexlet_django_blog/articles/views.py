from django.shortcuts import render


def index(request):
    name = 'Main page for articles'
    return render(request, 'articles/index.html', context={'name': name})
