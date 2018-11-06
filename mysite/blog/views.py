from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import BlogArticle
import json
import re

# Create your views here.
def blog_title(request):
    blogs = BlogArticle.objects.all()
    print(blogs)
    return render(request,"blog/titles.html",{"blogs":blogs})


def blog_article(request,article_id):
    # article = BlogArticle.objects.get(id=article_id)
    article = get_object_or_404(BlogArticle, id=article_id)
    print(article)
    publish = article.publish
    return render(request,"blog/content.html",{"article":article,"publish":publish})

def test(request):
    word = request.POST.get('hello')
    word = word.replace('\t','')
    try:
        word = json.loads(word)
    # with open('123.json', 'w', encoding='utf-8') as f:
    #     f.write(word)
    # f.close()
    # with open('123.json', 'r') as f:
    #     aa = json.load(f)
    #     print(aa)
        word = json.dumps(word)

    except :
        word = json.dumps(word)





    return HttpResponse(word)

def index(request):
    return render(request,'blog/index.html')