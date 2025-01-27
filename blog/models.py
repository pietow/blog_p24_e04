from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE) 
    body = models.TextField()

    def save(self, *args, **kwargs):
        counter = 1
        base_slug = f"{slugify(self.title)}-{counter}"
        while Post.objects.filter(slug=base_slug).exists():
            counter += 1
        self.slug = f"{slugify(self.title)}-{counter}"
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug": self.slug})


