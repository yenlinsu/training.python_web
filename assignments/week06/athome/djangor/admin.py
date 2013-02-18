from django.contrib import admin
from djangor.models import BlogPost

class BlogAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'title',
                    'published_today', 'owner')
    list_filter = ('pub_date', )
    ordering = ('pub_date', )

admin.site.register(BlogPost, BlogAdmin)