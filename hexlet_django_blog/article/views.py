from django.shortcuts import render
from django.views import View
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
       articles = Article.objects.all()[:15]
       return render(request, 'articles/articles.html', context={
           'articles': articles,
       })
    
def index(request, tags=None, article_id=None):
    return render(request, 'articles/article_index.html', context={'tags': tags, 'article_id': article_id})