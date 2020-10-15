from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

"""
-> SLUG: This is a field intended to be used in URLs. It contains only letters, numbers, underscores, 
or hyphens.
- You will use the slug field to build beautiful, SEO-friendly URLs for your blog posts.
  * You have added the unique_for_date parameter to this field so that you can build URLs for posts using 
  their publish date and slug.
  * Django will prevent multiple posts from having the same slug for a given date.

-> author: This field defines a many-to-one relationship, meaning that each post is written by a user, 
and a user can write any number of posts.

-> The Meta class inside the model contains metadata. You tell Django to sort results by the publish 
field in descending order by default when you query the database.

-> The __str__() method is the default human-readable representation of the object. Django will use it in 
many places, such as the administration site.
"""