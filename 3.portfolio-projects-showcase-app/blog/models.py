"""
    We need three separate database tables for the blog:
    1. Post
    2. Category
    2. Comment
    These tables need to be related to one another. 
    This is made easier because Django models come with fields specifically for this purpose.
"""
from django.db import models


class Category(models.Model):
    # Store the name of the category
    name = models.CharField(max_length=20)

class Post(models.Model):
    """
    The ManyToManyField takes two arguments. 
    The 1st is the model with which the relationship is, in this case its Category. 
    The 2nd allows us to access the relationship from a Category object, even though we haven’t added a field there. 
    Adding related_name of posts, we can access category.posts to give us a list of posts with that category.
    """
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    Categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    """
    We use another relational field, the ForeignKey field which defines a many to one relationship.
    The reasoning behind this is that many comments can be assigned to one post.
    But you can’t have a comment that corresponds to many posts.
    """
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)