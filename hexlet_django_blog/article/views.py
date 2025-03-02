from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    name = 'article'
    return render(
        request, 
        'articles/articles.html',
        context={'who': name})