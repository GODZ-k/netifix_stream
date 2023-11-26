from django.contrib import admin
from .models import *

# Register your models here.
class latest(admin.ModelAdmin):
    list_display=["update_name","update_description","updated_at","released_at"]

admin.site.register(Latestupdate,latest)