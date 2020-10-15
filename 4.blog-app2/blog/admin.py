from django.contrib import admin
from .models import Post

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    The list_display attribute allows you to set the fields of your model that you want to display on 
    the administration object list page.
    """
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # Customize the admin model with some more options
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')