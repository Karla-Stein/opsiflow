from django import forms
from django.forms.fields import EmailField
from django.forms.widgets import Textarea


class ContactUsForm(forms.Form):
    """
    A form to collect user messages.
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
