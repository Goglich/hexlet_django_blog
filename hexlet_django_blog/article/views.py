from django.shortcuts import render
from django.views import View
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect

class IndexView(View):

    def get(self, request):
        name = 'article'
        return redirect('article', tags='python', article_id=42)
    
def index(request, tags=None, article_id=None):
    return render(request, 'articles/article_index.html', context={'tags': tags, 'article_id': article_id})