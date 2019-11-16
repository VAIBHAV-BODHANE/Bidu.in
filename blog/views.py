from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

def index(request):

    blog = Blogpost.objects.all()
    params = {'blog': blog}
    return render(request,"blog/index.html", params)

def blogpost(request, id):
    blog = Blogpost.objects.filter(post_id= id)[0]
    print(blog)
    params = {'blog': blog}
    return render(request,"blog/blogpost.html", params)

