from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post> /', views.post_details, name='post_details'),
]

"""
    URL patterns allow you to map URLs to views.  
    Django runs through each URL pattern and stops at the first one that matches the requested URL.
    NOTE Namespace (app_name) variable. Allows you to organize URLs by application and use the name when 
    referring to them.
    - You use angle brackets to capture the values from the URL. 
    - Any value specified in the URL pattern as <parameter> is captured as a string. 
    - You use path converters, such as <int:year>, to specifically match and return an integer and 
    <slug:post> to specifically match a slug.
"""