from django.contrib.sitemaps import Sitemap
from projects.models import Project

class ProjectSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        if obj.end_date:
            return obj.end_date
        else:
            return obj.start_date