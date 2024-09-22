from django.contrib import admin

from blog.models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("heading", "content", "image", "view_count", "create_date")
