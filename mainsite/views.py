from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from datetime import datetime
from django.shortcuts import redirect
from django.template.loader import get_template


# Create your views here.

# 主页代码
def homepage(request):
    template = get_template('index.html')
    articles = Article.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)


# 显示单篇文章的代码
def show_article(request, slug):
    template = get_template('article.html')
    try:
        article = Article.objects.get(slug=slug)
        if article is not None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
