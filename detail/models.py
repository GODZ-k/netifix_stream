from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class Moviemanager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)

class Tags(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Tags'
class Categories(models.Model):
    category=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category

    class Meta:
        verbose_name_plural = 'Categories'

class movie(models.Model):
    category=models.ManyToManyField(Categories,related_name="categories")
    tags=models.ForeignKey(Tags,related_name="movie_tags",on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50, help_text="Enter the movie name")
    description=models.TextField(help_text="Enter the movie description")
    imdb_rating=models.FloatField( help_text="Enter the IMDb rating")
    movie_duration=models.CharField(max_length=20, help_text="Enter the movie duration Ex: 2h 34min")
    movie_year=models.IntegerField( help_text="Ex: 2024")
    movie_trailler=models.CharField(max_length=200 , help_text="Enter the youtube trailler video id Ex: aR_JzBGdGvM")
    movie_match=models.CharField(max_length=100, help_text="Ex: 67 ,Enter only number")
    movie_grade=models.CharField(max_length=200,help_text="Ex: U/A 18+")
    poster_portrait=models.URLField(max_length=900,help_text="Enter the movie poster URL Ex: http://...")
    director=models.CharField(max_length=200, help_text="Ex: Mark • David Hammer • Chris Green")
    cast=models.CharField(max_length=200,help_text="Ex: Chris hamesworth • Scarllet johnson")
    language=models.CharField(max_length=200 , help_text="Ex: English • Hindi")
    subtitle=models.CharField(max_length=200,help_text="Ex: English • Hindi • Spanish")
    quality=models.CharField(max_length=200 , help_text="Ex: 720p • 1080p • 2160p 60fps")
    screenshot_1=models.URLField(max_length=900, help_text="Enter the Screenshot 1 URL")
    screenshot_2=models.URLField(max_length=900, help_text="Enter the Screenshot 2 URl")
    screenshot_3=models.URLField(max_length=900, help_text="Enter the Screenshot 3 URL")
    screenshot_4=models.URLField(max_length=900, help_text="Enter the Screenshot 4 URL")
    screenshot_5=models.URLField(max_length=900, help_text="Enter the Screenshot 5 URL")
    screenshot_6=models.URLField(max_length=900, help_text="Enter the Screenshot 6 URL")
    update=models.CharField(max_length=100, default="No Updates" ,help_text="Ex: Episode 3 Added")
    slug=AutoSlugField(populate_from='movie_title',unique=True,null=True,default=None)
    movie_title=models.CharField(max_length=300, help_text="Ex: Loki full hd movie download")
    released_at=models.DateField(null=True , blank=True ,help_text=" Ex: 23/09/2021")
    updated_at=models.DateTimeField(auto_now=True)
    is_delete=models.BooleanField(default=False)

    objects=Moviemanager()
    admin_objects=models.Manager()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Add movies'

class trending(models.Model):
    poster_landscape=models.URLField(max_length=900)
    movies=models.ForeignKey(movie, related_name="trending_movies", on_delete=models.CASCADE)

    def __str__(self) ->str:
        return self.movies.name

    class Meta:
        verbose_name_plural = 'Trending Silder'

class hot_thrills(models.Model):
    movies=models.ForeignKey(movie, related_name="hot_thrills_movies", on_delete=models.CASCADE)
    label=models.CharField(max_length=200,null=True, blank=True)
    name_color=models.CharField(max_length=100 , default="grey")
    clip=models.FileField(upload_to="movie_media" ,help_text="If not clip url (Optional)",null=True,blank=True )
    clip_url=models.URLField(max_length=500 , null=True , blank=True, help_text="If not clip")
    clip_poster=models.URLField(max_length=300,help_text="Poster url (Optional)" , null=True, blank=True)
    text_image=models.URLField(max_length=200, null=True,blank=True,help_text="Image should be .png")
    text=models.CharField(max_length=50,null=True,blank=True,help_text="If not text_image ( Optional )")
    text_upload_image=models.ImageField(upload_to="movie_media" , null=True,blank=True,help_text="If not have text_image url ( Optional )")

    def __str__(self) -> str:
        return self.movies.name

    class Meta:
        verbose_name_plural = 'Hot Slideshow'

class poster1(models.Model):
    movie_wallpaper=models.ImageField(upload_to="movie_media")
    movies=models.ForeignKey(movie, related_name="poster1_movies", on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.movies.name

    class Meta:
        verbose_name_plural = 'Recommanded posters 1'


class poster2(models.Model):
    movie_wallpaper=models.ImageField(upload_to="movie_media")
    movies=models.ForeignKey(movie, related_name="poster2_movies", on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.movies.name

    class Meta:
        verbose_name_plural = 'Recommanded posters 2'


class poster3(models.Model):
    movie_wallpaper=models.ImageField(upload_to="movie_media")
    movies=models.ForeignKey(movie, related_name="poster3_movies", on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.movies.name

    class Meta:
        verbose_name_plural = 'Recommanded posters 3'