from django.urls import path,include
from .views import *

urlpatterns = [
    path("<slug>" , detail , name="detail")
]

