from django.db import models
from detail.models import *

# Create your models here.

class downloads(models.Model):
    movie_name=models.ForeignKey(movie, related_name='download',on_delete=models.CASCADE)

    # Quality 1

    Quality1=models.CharField(max_length=50,null=True,blank=True,help_text="Quality Ex: 420p")
    size1=models.CharField(max_length=50 , null=True,blank=True,help_text="Size of file Ex: 2GB")
    server1_1=models.URLField(max_length=500,null=True,blank=True,help_text="Download url")
    server2_1=models.URLField(max_length=500,null=True,blank=True,help_text="Download url")

    # Quality 2

    Quality2=models.CharField(max_length=50,null=True,blank=True,help_text="Quality Ex: 720p")
    size2=models.CharField(max_length=50 , null=True,blank=True,help_text="Size of file Ex: 2GB")
    server1_2=models.URLField(max_length=500,null=True,blank=True,help_text="Download url")
    server2_2=models.URLField(max_length=500,null=True,blank=True,help_text="Download url")

    # Quality 3

    Quality3=models.CharField(max_length=50,null=True,blank=True,help_text="Quality Ex: 1080p")
    size3=models.CharField(max_length=50 , null=True,blank=True,help_text="Size of file Ex: 2GB")
    server1_3=models.URLField(max_length=500,null=True,blank=True,help_text="Download url")
    server2_3=models.URLField(max_length=500,null=True,blank=True,help_text="Download url")

    # Quality 4

    Quality4=models.CharField(max_length=50,null=True,blank=True,help_text="Quality Ex: 2160p")
    size4=models.CharField(max_length=50 , null=True,blank=True,help_text="Size of file Ex: 2GB")
    server1_4=models.URLField(max_length=500,null=True,blank=True,help_text="Download url")
    server2_4=models.URLField(max_length=500,null=True,blank=True,help_text="Download url")

    def __str__(self):
        return self.movie_name.name
    class Meta:
     verbose_name = 'Downloads'
     verbose_name_plural = 'Downloads'