from django.db import models

# Create your models here.
class Latestupdate(models.Model):
    update_name=models.CharField(max_length=400,null=True,blank=True,help_text="Enter the update name")
    update_description=models.TextField(null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True)
    released_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Latest updates'