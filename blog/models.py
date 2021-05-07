from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='public/')
    slug = models.SlugField()
    short_description = models.TextField()
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("blog:blog_details", kwargs={

            "slug": self.slug

            })
    