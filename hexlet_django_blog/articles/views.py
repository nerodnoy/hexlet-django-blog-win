from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        name = 'Main page for articles'
        return render(request, 'articles/index.html',
                      context={
                          'name': name
                      })
