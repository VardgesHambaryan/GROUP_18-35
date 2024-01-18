from django import forms
from .models import StayUpdated , ContactUs , Checkout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
        
class StayUpdatedForm(forms.ModelForm):
    class Meta:
        model = StayUpdated
        fields = ['email']

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
  
class CheckoutForm(forms.ModelForm):
	class Meta:
		model = Checkout
		fields = '__all__'