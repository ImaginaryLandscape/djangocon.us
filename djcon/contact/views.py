from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext

from djcon.contact.settings import use_submitpath
from djcon.contact.forms import ModelContactUsForm
from djcon.contact import models
from djcon.contact.utils import email_all


def index(request):
    if use_submitpath:
        form = ModelContactUsForm(initial={'contact_submit_path': request.get_full_path()})
    else:
        form = ModelContactUsForm()        
    if request.method == 'POST':
        form = ModelContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            email_all(request, form)
            return HttpResponseRedirect(reverse('contactus_sent'))
    return render_to_response('contact/contact_form.html',
                              {'form':form},
                              context_instance=RequestContext(request))


def sent(request):
    return render_to_response('contact/sent.html', {}, 
        context_instance=RequestContext(request))


