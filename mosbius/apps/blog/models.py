from django.db import models
from django.contrib.admin.models import User
from django.core.urlresolvers import reverse
from django.contrib.sitemaps import ping_google

from tagging.fields import TagField

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    tags = TagField()
    body = models.TextField()
    published = models.BooleanField()
    posted_by = models.ForeignKey(User)
    posted_on = models.DateTimeField(auto_now_add=True)
    
    def save(self, force_insert=False, force_update=False):
        super(Post, self).save(force_insert, force_update)
        try:
            ping_google()
        except:
            pass

    @models.permalink
    def get_absolute_url(self):
        return('blog_post_detail',(),
            {
                'year': self.posted_on.year,
                'month': self.posted_on.month,
                'day': self.posted_on.day,
                'slug': self.slug,
            })
        
    def __unicode__(self):
        return "%s (%s - %s)" % (self.title, self.posted_by, self.posted_on)
        
    class Meta:
        ordering = ['-posted_on']
        