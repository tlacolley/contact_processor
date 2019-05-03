
from django.template import RequestContext
from django.shortcuts import render , render_to_response, redirect

from contact_form.forms import ContactForm  


# Processor for the contact for on every page
def contact_processor(request):
    return {'contact_form': ContactForm(request=request)}








