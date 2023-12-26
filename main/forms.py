from django import forms
from .models import StayUpdated , ContactUs

class StayUpdatedForm(forms.ModelForm):
    class Meta:
        model = StayUpdated
        fields = ['email']

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
  