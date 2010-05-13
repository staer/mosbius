from django.conf.urls.defaults import *
from blog.models import Post

urlpatterns = patterns('',
    # Latest 
    url(r'^$', 
        'django.views.generic.date_based.archive_index',
        {
            'queryset': Post.objects.filter(published=True),
            'date_field': 'posted_on',
            'num_latest': 5,
            'template_object_name': 'posts',
        }, name="blog_post_latest"),
    
    # Year Archive
    url(r'^(?P<year>\d{4})/$',
        'django.views.generic.date_based.archive_year',
        {
            'queryset': Post.objects.filter(published=True),
            'date_field': 'posted_on',
        }, name="blog_post_archive_year"),    
    
    # Month Archive
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
        'django.views.generic.date_based.archive_month',
        {
            'queryset': Post.objects.filter(published=True),
            'date_field': 'posted_on',
            'month_format': '%m',
            'template_object_name': 'post',
        }, name="blog_post_archive_month"),
        
    # Day Archive
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
        'django.views.generic.date_based.archive_day',
        {
            'queryset': Post.objects.filter(published=True),
            'date_field': 'posted_on',
            'month_format': '%m',
            'template_object_name': 'post',
        }, name="blog_post_archive_day"),
    
    # Post Detail
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        'django.views.generic.date_based.object_detail',
        {
            'queryset': Post.objects.filter(published=True),
            'date_field': 'posted_on',
            'template_object_name': 'post',
            'month_format': '%m',
        }, name='blog_post_detail'),
        
    # Tag listing
    url(r'^tags/(?P<tag>[^/]+)/$',
        'tagging.views.tagged_object_list',
        {
            'queryset_or_model': Post,
            'template_object_name': 'post',
            'template_name': 'blog/tag_list.html',
        }, name='blog_tag_list'),
)