from django import forms
from STPApp import models

from django.core.mail import send_mail
from django.conf import settings

class ClientForm(forms.ModelForm):

    class Meta:
        model = models.Client
        fields = ('name','email','contact')

        widget = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'})
        }

class TravelGuideForm(forms.ModelForm):
    class Meta:
        model = models.TravelGuide

        fields = '__all__'