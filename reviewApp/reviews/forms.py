from django import forms
#from django.contrib.auth.models import User
#from .models import Profile

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	subject = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)

	class Meta:
		fields = ['name', 'email', 'subject', 'message']