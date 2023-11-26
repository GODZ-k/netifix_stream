from django.db import models

# Create your models here.
class Latestupdate(models.Model):
    update_name=models.CharField(max_length=400,null=True,blank=True,help_text="Enter the update name")
    update_description=models.TextField(null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True)
    released_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Latest updates'


class Browse_update(models.Model):
    browse_name=models.CharField(max_length=50,help_text="Enter the movie name")
    browse_url=models.URLField( max_length=200,null=True,blank=True,help_text="If not poster image ")
    browse_image=models.ImageField(upload_to="movie_media",help_text="If not image url", null=True, blank=True)
    browse_clip=models.URLField(max_length=1000 , help_text="If have clip url (optional)",null=True,blank=True)
    browse_trailler=models.CharField(max_length=900,help_text="Enter the trailler id")
    browse_release_date=models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    coming=models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Browse slideshow'
        verbose_name_plural = 'Browse slideshow'