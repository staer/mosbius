from django.contrib import admin
from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'teaser']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body']
    ordering = ['title']

admin.site.register(Project, ProjectAdmin)