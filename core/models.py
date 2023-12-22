from django.db import models

# Create your models here.
class Subscribers(models.Model):
    Email=models.CharField(max_length=500,null=True)

    def __str__(self) -> str:
        return self.Email

    class Meta:
        verbose_name_plural = 'Subscribers'