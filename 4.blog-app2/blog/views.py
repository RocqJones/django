from django.shortcuts import render, get_object_or_404
from .models import Post

# create a list and a detailed view
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_details(request, year, month, day, post):
    # get_object_or_404() shortcut to retrieve the desired post.
    post = get_object_or_404(Post, slug = post, status = 'published', 
                            publish__year = 'year',
                            publish__month = 'month',
                            publish__day = 'day')

    return render(request, 'blog/post/detail.html', {'post': post})