from django.db import models
from tinymce.models import HTMLField

class BlogPost(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length = 100)
    text = HTMLField()
    featured_image = models.ImageField(upload_to='', blank=True)
    draft_status = models.NullBooleanField(default=None)
    description = models.CharField(max_length = 160, blank=True, null=True)
    slug = models.SlugField(max_length=100, default="#")
    
    def __str__(self):
        return self.title
  
    def get_absolute_url(self):
        return f"/blog/{self.slug}/"

class Project(models.Model):
    title = models.CharField(max_length = 100)
    link = models.CharField(max_length = 100)
    about = HTMLField()
    featured_image = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.title