from django.contrib.sitemaps import Sitemap
from .models import BlogPost
 
 
class PostSitemap(Sitemap):    
   changefreq = "monthly"
   priority = 0.9
 
   def items(self):
      return BlogPost.objects.all()