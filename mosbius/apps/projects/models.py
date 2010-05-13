from django.db import models
from django.contrib.sitemaps import ping_google

class Project(models.Model):
    title = models.CharField(max_length=200, help_text="The title of the project")
    slug = models.SlugField(help_text="Slug to use in the URL for the project")
    teaser = models.TextField(help_text="Short description of the project for use in listings")
    body = models.TextField(help_text="Full description of the project")
    start_date = models.DateTimeField(help_text="Project start date", blank=True, null=True)
    end_date = models.DateTimeField(help_text="Project end date", blank=True, null=True)
    source_code = models.URLField(help_text="Url to source repository, or project hosting page", blank=True)
    
    def save(self, force_insert=False, force_update=False):
        super(Project, self).save(force_insert, force_update)
        try:
            ping_google()
        except:
            pass
    
    @models.permalink
    def get_absolute_url(self):
        return("project_detail",(),{'slug': self.slug})
    
    def __unicode__(self):
        return self.title
        
    class Meta:
        ordering = ['title']
        
    def has_summary(self):
        """ Checks to see if the project has any summary information """
        if self.start_date or self.end_date or self.source_code:
            return True
        else:
            return False