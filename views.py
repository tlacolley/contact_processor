from django.shortcuts import render ,render_to_response, redirect

from django.template import RequestContext

# Create your views here.
from django.views.generic import TemplateView
# import the form from django-contact-form? 
from contact_form.forms import ContactForm 

from django.http import HttpResponse

# Create your views here.



class IndexView(TemplateView):
    template_name = 'haa_core/index.html'


    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            
            form = ContactForm(request=request)
            # return render(request, 'haa_contact/contact_form/contact_form_sent.html')
            print("Home: Thanks -----------------------")
            return redirect('home:thanks')
            # reverse('myapp:my_url_name')

        else:
            return ContactForm(request=request)

