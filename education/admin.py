from django.contrib import admin
from .models import Article, Video

# Register Article with a custom admin class (only once)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published')
    list_filter = ('category', 'published')

# Register Video (only once)
admin.site.register(Video)
