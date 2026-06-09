from django.shortcuts import render
from django.http.response import HttpResponseRedirect 
from django.conf import settings
import resend
from django.contrib import messages

from .forms import ContactUsForm 



def index(request):
    """
    A view to return the index page
    """
    return render(
        request,
        'home/index.html'
    )

def contact_us_view(request): 
   """
   A view to send a message to platfoem owner once new message was submitted.
   """
   resend.api_key = settings.RESEND_KEY

   if request.method == "POST": 
       form = ContactUsForm(request.POST) 
       if form.is_valid(): 
           name = form.cleaned_data["name"]
           email = form.cleaned_data["email"]
           subject = form.cleaned_data["subject"]
           message = form.cleaned_data["message"]

           resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": "karlasteinbrink@gmail.com",
                "subject": "Hello World",
                "html": "<h2>New Message!</h2>"
                        f"<p><strong>Name:</strong> {name}</p>"
                        f"<p><strong>Email:</strong> {email}</p>"
                        f"<p><strong>Subject:</strong> {subject}</p>"
                        f"<p><strong>Message:</strong></p>"
                        f"<p>{message}</p>"
                        
                })
           messages.success(request, (
                    "Thank you for your message! We will be in touch shortly!"
                ))


           return HttpResponseRedirect('/') 
   else: 
       form = ContactUsForm() 

   return render(request, 
                 "home/contact.html", 
                 {'form':form})


