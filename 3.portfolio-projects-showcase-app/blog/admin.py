from django.contrib import admin
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

# Note: We’re not adding the comments to the admin. 
# That’s because it’s not usually necessary to edit or create comments yourself.