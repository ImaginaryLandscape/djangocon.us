from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext

from djcon.contact.utils import email_all
from djcon.contact.settings import use_submitpath
from djcon.contact.forms import ModelContactUsForm

class ContactFormMiddleware(object):
    def process_request(self, request):
        if request.method == 'POST' and 'is_contact' in request.POST:
            # validate the form
            form = ModelContactUsForm(data=request.POST)
            if form.is_valid():
                form.save()
                email_all(request, form)
                form.submit_success = True
        else:
            if use_submitpath:
                form = ModelContactUsForm(initial={'contact_submit_path': request.get_full_path()})
            else:
                form = ModelContactUsForm()

        request.contact_form = form
