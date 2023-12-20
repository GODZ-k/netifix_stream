"""
URL configuration for Netifix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Netifix import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
# debug = false
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    # fake admin pannel
    path('admin/', include('admin_honeypot.urls')),

    # actual admin pannel
    path('django_admin/clearcache/', include('clearcache.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),  # whitenoise if debug = False
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), # whitenoise if debug = False
    path('django_admin/', admin.site.urls),

    # path("django-check-seo/", include("django_check_seo.urls")),    # django-check-seo

    path("",include("core.urls")),
    path("detail/", include("detail.urls")),


]

if settings.DEBUG:  # Dev only
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns+=staticfiles_urlpatterns()
