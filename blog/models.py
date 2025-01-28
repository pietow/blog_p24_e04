from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE) 
    body = models.TextField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post_detail', kwargs={"pk": self.id})

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        self.slug = base_slug
        return super().save(*args, **kwargs)


