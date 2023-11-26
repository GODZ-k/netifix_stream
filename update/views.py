from django.shortcuts import render
from .models import *

# Create your views here.
def latestupdate():
    update=Latestupdate.objects.all()
    return {
        "update": update,
    }