from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    post_body = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True, blank=True)

    def _str_(self):
        return self.title