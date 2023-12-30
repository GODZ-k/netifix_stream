from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from detail.models import movie,Categories,Tags

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'dmca', 'about','netflix','disneyplus','amazonprime','Browse','hbo']

    def location(self, items):
        return reverse(items)



class PostViewSitemap(Sitemap):
    def items(self):
         return movie.objects.all()



class CategoryViewSitemap(Sitemap):
    def items(self):
        return Categories.objects.all()


class TagsViewSitemap(Sitemap):
    def items(self):
        return Tags.objects.all()
