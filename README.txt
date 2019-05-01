
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




For Using SendGrid 


use the SendGrid STMP


Check the path in the URLS 







Create a form where you want, like in the footer.html 


   


