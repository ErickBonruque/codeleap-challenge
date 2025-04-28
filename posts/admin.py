from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('username', 'title', 'created_datetime')
    list_filter = ('username', 'created_datetime')
    search_fields = ('title', 'content', 'username')
    date_hierarchy = 'created_datetime'
