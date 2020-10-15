from django.contrib import admin
from .models import Post

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # Customize the admin model with some more options
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

    """
    - The list_display attribute allows you to set the fields of your model that you want to display on 
    the administration object list page.
    - As you type the title of a new post, the slug field is filled in automatically. You've told Django to
    prepopulate the slug field with the input of the title field using the "prepopulated_fields" attribute.
    - "raw_id_fields" the author field is now displayed with a lookup widget that can scale much better 
    than a drop-down select input when you have thousands of users.
    """