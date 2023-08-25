from django.db import models

# Create your models here.
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # categories = models.ManyToManyField('Category', blank=True)

    class Meta:
        ordering = ['created']

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', related_name='categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'