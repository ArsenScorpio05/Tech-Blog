from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, Topic
# Create your views here.

def welcomePage(request):
    
    context = {
        "matches": Blog.objects.all(),
        
    }
    
    return render(request, "base/welcomePage.html", context)

def aboutPage(request):
    
    context = {
        "matches": Blog.objects.all(),
        
    }
    
    return render(request, "base/about.html", context)

def blogArticles(request):
    
    context = {
        "matches": Blog.objects.all(),
        
    }
    
    return render(request, "base/blog.html", context)
