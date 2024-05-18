from django.shortcuts import render


def index(request):
    name = 'Main page for article'
    return render(request, 'article/index.html', context={'name': name})
