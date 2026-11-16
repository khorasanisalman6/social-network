from django.contrib import admin

from blog.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created', 'updated']
    list_filter = ['created', 'updated']