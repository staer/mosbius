from django.conf.urls.defaults import *
from django.contrib.sitemaps import FlatPageSitemap
from blog.sitemaps import BlogSitemap
from blog.feeds import LatestPosts
from projects.sitemaps import ProjectSitemap

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

sitemaps = {
    'flatpages': FlatPageSitemap,
    'blog': BlogSitemap,
    'project': ProjectSitemap,
}

feeds = {
    'blog': LatestPosts,
}

urlpatterns = patterns('',
    (r'^contact/', include('contact_form.urls')),
    (r'', include('blog.urls')),
    (r'^projects/', include('projects.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^robots.txt$', 'django.views.generic.simple.direct_to_template', {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    url(r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}, name="blog_feed"),
)

# Check to see if DEBUG=True
# If yes, then Django should serve media files
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }, name='media'),
    )
