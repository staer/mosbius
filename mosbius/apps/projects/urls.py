from django.conf.urls.defaults import *
from projects.models import Project

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', 
        {
            'queryset': Project.objects.all(),
            'template_object_name': 'project',
        }, name="projects_list"),
    
    # Object detail
    url(r'^(?P<slug>[\w-]+)/$', 'django.views.generic.list_detail.object_detail',
        {
            'queryset': Project.objects.all(),
            'template_object_name': 'project',
        }, name="project_detail"),
)