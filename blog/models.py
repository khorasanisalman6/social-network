from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='posts')
    title = models.CharField(max_length = 100 )
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    status = models.BooleanField(default=False)
    slug = models.SlugField(max_length = 100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'