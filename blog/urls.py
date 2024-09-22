from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import main_page, ArticleDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('', cache_page(60)(main_page), name='blog_main'),
    path('detail/<int:pk>', cache_page(60)(ArticleDetailView.as_view()), name='blog_detail'),
]