from django.conf.urls.defaults import patterns

urlpatterns=patterns('djcon.contact.views',
    (r'^$', 'index', {}, 'contactus_index'),
    (r'^sent/$', 'sent', {}, 'contactus_sent'),
)
