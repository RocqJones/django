# The final step before you get to create the templates and actually see this blog up and running is 
# to hook up the URLs.
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
]

# Once the blog-specific URLs are in place, you need to add them to the projects URL configuration 
# using include()