from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = { 'posts': posts }
    return render(request, 'blog_index.html', context)

def blog_category(request, category):
    # The filter argument tells Django what conditions need to be met for an object to be retrieved
    posts = Post.objects.filter(categories__name__contains = category).order_by('-created_on')
    context = { 
        'category': category, 
        'posts': posts 
    }
    return render(request, 'blog_category.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    # Once you’ve created the comment from the form, you’ll need to save it using save() and then query 
    # the database for all the comments assigned to the given post...(continue here after 'forms.py')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                post = post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = { 
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog_detail.html', context)

    """
    - When a form is posted, a POST request is sent to the server. 
    - So, in the view function, we need to check if a POST request has been received. 
    - We can then create a comment from the form fields. 
    - Django comes with a handy is_valid() on its forms, so we can check that all the fields have been 
    entered correctly.
    """