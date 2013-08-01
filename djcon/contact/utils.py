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
    sender_email = request.POST.get('contact_email', '')
    sender_name = request.POST.get('contact_name', '')    
    from_email = getattr(settings, 'SERVER_EMAIL', 'webmaster@djangocon.us')
    email_subject_prefix = getattr(settings, 'EMAIL_SUBJECT_PREFIX', '')
    recipients = getattr(settings, 'MANAGERS', 'webmaster@djangocon.us')
    if sender_name:
        email_headers = {'Reply-To': "%s <%s>" % (sender_name, sender_email)}
    else:
        email_headers = {'Reply-To': sender_email}
    try:
        mail_subject = '%s%s' % (email_subject_prefix, 
            form.cleaned_data['contact_subject'])
    except:
        mail_subject = '%s%s' % (email_subject_prefix, getattr(
            settings, 'CONTACT_SUBJECT', 'New contact form at %s' % site))
    email = EmailMessage(mail_subject, msg_admin, from_email, [a[1] for a in recipients],
        headers = email_headers)
    email.send() 
    return
