from django.contrib import admin
from news.models import Article


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'status', 'author', 'published_at')
    list_display_links = ('id', 'title')
    list_filter = ('id', 'title', 'status', 'author', )

    fields = ('title', 'slug', 'content', 'short_content', 'status', 'author')

    empty_value_display = '😱'
    
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Article, ArticleAdmin)