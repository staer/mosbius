from django.contrib import admin
from blog.models import Post

def make_published(modeladmin, request, queryset):
    queryset.update(published=True)
make_published.short_description = "Mark selected items as published"

def make_unpublished(modeladmin, request, queryset):
    queryset.update(published=False)
make_unpublished.short_description = "Mark selected items as unpublished"

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'posted_on'
    list_display = ('title', 'published', 'posted_by', 'posted_on')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body']
    ordering = ['-posted_on',] 
    
    # Use a custom change form so that we can see a preview of what the
    # rendered post will look like
    change_form_template = "blog/admin/post_change_form.html"   
    
    # Custom admin actions
    actions = [make_published, make_unpublished]
    
admin.site.register(Post, PostAdmin)