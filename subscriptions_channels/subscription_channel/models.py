from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, db_index = True)
    slug = models.SlugField(max_length=150, unique = True)
    body = models.TextField(blank=True)
    date_pub = models.DateTimeField(auto_now_add = True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        db_table = 'posts'


class PaidContent(models.Model):
    content_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    content_html = models.TextField()

    class Meta:
        db_table = 'paid_content'
