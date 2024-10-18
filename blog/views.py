from django.shortcuts import render
from .models import Post

def index(request):
    context = {
        "posts" : Post.objects.all,
    }
    return render(request, "index.html", context)

def contact(request):
    return render(request, "contact.html")

def post(request):
    return render(request, "post.html")

def about(request):
    return render(request, "about.html")