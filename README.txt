
Create a context_processors with Django-contact-form



1) Install contact_form and App------------------------------------------

First install Django-contact-form, 
Add 'contact_form' and this App in yout INSTALLED_APPS  in 'setting.py' like this:




In setting.py 

INSTALLED_APPS = [
    ... ,
    ... ,
    'contact_form',
    'haa_contact',


]


2) context_processors install------------------------------------------

In TEMPLATES, OPTIONS, contact_processor add the path to the contact_processor file :  'haa_core.context_processors.contact_processor'


TEMPLATES = [
    {
    'OPTIONS': {
        'context_processors': [
            ' HERE  '
        ]
        },
    },
]



3) Console Test-------------------------------------------

For this contact form I will test it with the console return 
At the end of 'setting.py' add this:

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



4) Urls -------------------------------------------

In your urls.py file add the path to contact_form urls like this


urlpatterns = [
    ... ,
    ... ,
    path('contact/', include('contact_form.urls')),
]



5) Templates ---------------------------------------

You can Create a form where you want, like in the footer.html 


         <h4>Contact us</h4>
            <form method="post" action="{% url 'contact_form' %}" class="text-center px-5 mt-5">{% csrf_token %}

                <!-- Here for render the context-contact_processor -->
                
                {% render_field contact_form.name  placeholder=contact_form.name.label %}
                {% render_field contact_form.email    placeholder=contact_form.email.label %}
               
                {% render_field contact_form.body  placeholder=contact_form.body.label %}

                <button type="submit" class=""> Submit </button>
            </form>


The form action redirect to the contact_form urls 
To render the field I use here the render_field form Contact-form








For Using SendGrid SMTP, Official Documentation ( links )

At the end of setting.py change or add 


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.sendgrid.net'  
EMAIL_PORT = 587  
EMAIL_HOST_USER = 'apikey'  # this is SendGrid username don't change it


For the EMAIL_HOST_PASSWORD is better to used an variable in an other files and import it just before 

from project.extra_settings import *

EMAIL_HOST_PASSWORD = '[Your scripted key here / my variable api_key_code from extra_settings.py ]'   # set environ yourself 
Put the Apikey generate by SendGrid not in Base64


ADMINS = (
    ('[Yourname]', 'apikey'),   # email will be sent to your_email
)

MANAGERS = ADMINS













