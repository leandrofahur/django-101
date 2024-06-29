from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'author', 'is_liked')
    search_fields = ('title', 'author')
    list_filter = ('rating', 'is_liked')