# email composition live here

from django.core.mail import mail_managers, EmailMessage
from django.conf import settings
from django.template import loader, RequestContext
from django.contrib.sites.models import Site

template_admin = 'contact/contact_email_admin.txt'
template_sender = 'contact/contact_email_sender.txt'

def email_all(request, form):
    site=Site.objects.get_current()
    context = RequestContext(request,
        dict(form.cleaned_data, site=site, contact=form.instance))

    # getting e-mail messages from according templates
    msg_admin = loader.render_to_string(template_admin, context)
    msg_sender = loader.render_to_string(template_sender, context).strip()
    try:
        mail_subject = form.cleaned_data['contact_subject']
    except:
        mail_subject = getattr(settings, 'CONTACT_SUBJECT', 'New contact form at %s' % site)
    # notify managers
    mail_managers(mail_subject, msg_admin, True)
    return
