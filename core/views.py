from django.shortcuts import render
from detail.models import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    # pagination and search
    _items=movie.objects.all()
    searching_pagination=search_pagination(request,_items)

    # hot thrills
    hot_thrill_data_dict=hot_thirill_data()
    # recommanded poster
    poster_data=poster()
    # category
    category_data_dict=category_data()
    # movie tags
    movie_tags=tags()
    # trending
    movie_trend=trend()

    data={
        # pagination and search
        **searching_pagination,
       # hot thrills
        **hot_thrill_data_dict,
        # recommanded poster
        **poster_data,
        # movie trend
        **movie_trend,
        # movie tags
        **movie_tags,
        # category data
        **category_data_dict,

    }
    return render(request, "index.html",data)

def category_data():
    Scifi=movie.objects.filter(category__category="Scifi")
    Action=movie.objects.filter(category__category="Action")
    Advanture=movie.objects.filter(category__category="Advanture")
    Comedy=movie.objects.filter(category__category="Comedy")
    Fantasy=movie.objects.filter(category__category="Fantasy")
    History=movie.objects.filter(category__category="History")
    Horror=movie.objects.filter(category__category="Horror")
    Thriller=movie.objects.filter(category__category="Thriller")
    Mystery=movie.objects.filter(category__category="Mystery")
    Romance=movie.objects.filter(category__category="Romance")

    return {
        "Scifi": Scifi,
        "Action": Action,
        "Advanture": Advanture,
        "Comedy": Comedy,
        "Fantasy": Fantasy,
        "History": History,
        "Horror": Horror,
        "Thriller": Thriller,
        "Mystery": Mystery,
        "Romance": Romance,
    }

def hot_thirill_data():
    hot_thrill=hot_thrills.objects.all()
    return {
        "slideshow": hot_thrill,
    }

def poster():
    recomanded1=poster1.objects.all()
    recomanded2=poster2.objects.all()
    recomanded3=poster3.objects.all()

    return {
        "recomanded1":recomanded1,
        "recomanded2":recomanded2,
        "recomanded3":recomanded3,
    }

def tags():
    movie_tags=Tags.objects.all()

    return {
        "movie_tags":movie_tags,
    }


def trend():
    trend=trending.objects.all()

    return {
      "trend":trend,
    }

def dmca(request):
    return render(request,"dmca.html")

def About(request):
    return render(request,"About.html")

def Netflix(request):
    _items=movie.objects.filter(tags__name="Netflix")
    searching_pagination=search_pagination(request,_items)

    data={
        **searching_pagination
    }

    return render(request,"Netflix.html",data)

def disneyplus(request):
    _items=movie.objects.filter(tags__name="Disney+")
    searching_pagination=search_pagination(request,_items)

    data={
        **searching_pagination
    }

    return render(request,"disney+.html",data)


def Amazonprime(request):
    _items = movie.objects.filter(tags__name="Prime")
    searching_pagination=search_pagination(request,_items)

    data={
        **searching_pagination
    }

    return render(request,"Amazonprime.html",data)

def Browse(request):
    return render(request,"Browse.html")

def HBO(request):
    _items=movie.objects.filter(tags__name="HBO")
    searching_pagination=search_pagination(request,_items)

    data={
        **searching_pagination
    }

    return render(request,"HBO.html",data)

# searching and pagination functions for tags items
def search_pagination(request,_items):
    items=_items   # for better understanding
    if request.method == 'GET':
        search=request.GET.get('search','')
        if search != '':
            items = _items.filter(name__icontains=search)

    paginatordata=Paginator(items,1)
    page_no=request.GET.get("page")
    finaldata=paginatordata.get_page(page_no)
    lastpage=finaldata.paginator.num_pages
    total_page_no=[n+1 for n in range(lastpage)]
    return {
        "items": finaldata,
        "lastpage":lastpage,
        "total_page_no":total_page_no,
        "search":search,
    }
