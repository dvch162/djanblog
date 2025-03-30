from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post, Category

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Category.objects.all()

    
class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)
    
    def lastmod(self, item):
        return item.created_at