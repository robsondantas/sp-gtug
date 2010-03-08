# -*- coding: utf-8 -*-
# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from models import Post

def index(request):
    post_list = Post.objects.all().order('-pub_date')[:5] #lista 5 ultimas ordenados por data
    t = loader.get_template('gtug/index.html')
    c = Context({'posts' : post_list})
    
    return HttpResponse(t.render(c))
