from django.shortcuts import render
from .models import *

# Create your views here.
def detail(request,slug):
    items=movie.objects.get(slug=slug)
    related_items=movie.objects.filter(category__in=items.category.all()).exclude(slug=slug)[:30]
    data={
        "items":items,
        "related_items":related_items,
    }
    return render(request,"detail.html",data)
