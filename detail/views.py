from django.shortcuts import render
from .models import *

# Create your views here.
def detail(request,slug):
    items=movie.objects.get(slug=slug)
    data={
        "items":items
    }
    return render(request,"detail.html",data)
