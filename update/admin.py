from django.contrib import admin
from .models import *

# Register your models here.
class latest(admin.ModelAdmin):
    list_display=["update_name","update_description","updated_at","released_at"]

class Browseupdate(admin.ModelAdmin):
    list_display=["browse_release_date","browse_name","browse_clip","browse_url","browse_image","browse_trailler","coming"]

admin.site.register(Latestupdate,latest)
admin.site.register(Browse_update,Browseupdate)