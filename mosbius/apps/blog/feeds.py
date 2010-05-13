from django.contrib.syndication.feeds import Feed
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.syndication.feeds import FeedDoesNotExist
from django.core.urlresolvers import reverse

from blog.models import Post
from tagging.models import Tag

class LatestPosts(Feed):
    
    def get_object(self, bits):
        """ Check to see if the user is requesting a feed for a specific tag 
        used in a post"""
        if len(bits)==1:
            return Tag.objects.get(name__iexact=bits[0])
        elif len(bits)==0:
            return None
        else:
            raise ObjectDoesNotExist
        
    def title(self, obj):
        if obj:
            return "mosbius.com: posts tagged as '%s'" % obj.name
        else:
            return "mosbius.com"
    
        
    def description(self, obj):
        if obj:
            return "recent blog posts tagged under '%s'" % obj.name
        else:
            return "recent blog posts"
            
          
    def link(self, obj):
        if obj:
            return reverse('blog_tag_list', kwargs={'tag': obj.name})
        else:
            return reverse('blog_post_latest')
        
    def items(self, obj):
        if obj:
            return Post.objects.filter(published=True).filter(tags__contains=obj)[:10]
        else:
            return Post.objects.filter(published=True)[:10]
