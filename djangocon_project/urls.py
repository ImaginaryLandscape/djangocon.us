from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer

from djangocon_project.views import creole_preview


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {
        "template": "homepage.html",
    }, name="home"),

    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^openid/", include(PinaxConsumer().urls)),
    url(r"^blog/", include("biblion.urls")),
    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposal/", include("symposion.proposals.urls")),
    url(r"^review/", include("symposion.review.urls")),
    url(r"^about/", include("about.urls")),
    url(r"^schedule/", include("symposion.schedule.urls")),
    url(r"^creole_preview/$", creole_preview, name="creole_preview"),
    url(r'^markitup/', include('markitup.urls')),
    url(r'^galleries/', include('photologueext.urls')),
    url(r"^wiki/", include("wakawaka.urls")),
)

if settings.SERVE_MEDIA:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
