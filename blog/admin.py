from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author' ,'datetime_created', 'datetime_modified')

#admin.site.register(Post, PostAdmin)