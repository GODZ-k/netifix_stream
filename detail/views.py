from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.
def detail(request,slug):
    items = get_object_or_404(movie, slug=slug)
    related_categories=items.category.all().distinct()
    related_tags=movie.objects.filter(tags=items.tags).exclude(slug=slug).distinct()[:20]
    data={
        "items":items,
        "related_categories": related_categories,
        "related_tags":related_tags
        }
    return render(request,"detail.html",data)
