from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ContactApp(CMSApp):
    name = _("Iscape Contact Form") # give your app a name, this is required
    urls = ["djcon.contact.urls"] # link your app to url configuration(s)

apphook_pool.register(ContactApp) # register your app
