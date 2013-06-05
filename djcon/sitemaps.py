from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap
from symposion.cms.models import Page

class ViewSitemap(Sitemap):
    """Reverse static views for XML sitemap."""
    def items(self):
        # Return list of url names for views to include in sitemap
        return ['home','schedule_conference','sponsor_list','account_signup','account_login']

    def location(self, item):
        return reverse(item)

class CMSSitemap(Sitemap):
    def items(self):
        return Page.published.all()
