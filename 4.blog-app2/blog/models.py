from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Part 4: model manager.
class PublishedManager(models.Manager):
    def get_query_set(self):
        return super(PublishedManager, self).get_query_set().filter(status='published')

# Part 2
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

    # call manager (extends Part 4)
    objects = models.Manager() # default manager
    published = PublishedManager() # our custom manager

    # Part 8: Canonical URLs for models
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, 
                                                self.publish.month, 
                                                self.publish.day, self.slug])

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

-> Canonical URL is the preferred URL for a resource. 
   * You may have different pages in your site where you display posts, but there is a single URL that you 
   use as the main URL for a blog post. 
   * The convention in Django is to add a get_absolute_url() method to the model that returns the 
   canonical URL for the object.
"""