from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["created_date", "published_date"]
    fields = ["author", "title", "text", "created_date", "published_date"]


