from django.shortcuts import render,get_object_or_404
from .models import *
from downloads.models import *
# Create your views here.
def detail(request,slug):
    items = get_object_or_404(movie, slug=slug)
    related_categories=items.category.all().distinct()
    related_tags=movie.objects.filter(tags=items.tags).exclude(slug=slug).distinct()[:20]
    download_detail=download()
    data={
        "items":items,
        "related_categories": related_categories,
        "related_tags":related_tags,
        **download_detail,
        }
    return render(request,"detail.html",data)


def download():
    download_movie=downloads.objects.all()
    return{
        "download":download_movie,
    }