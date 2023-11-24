from django.urls import path
from .views import *

urlpatterns = [
    path("" , home , name="home"),
    path("Dmca/",dmca, name="dmca"),
    path("About/", About ,name="about"),
    path("Netflix/",Netflix,name="netflix"),
    path("Disney+/",disneyplus,name="disneyplus"),
    path("Amazonprime/",Amazonprime,name="amazonprime"),
    path("Browse/",Browse ,name="Browse"),
    path("HBO/",HBO,name="hbo"),
    path("404/",error, name="error")
]

