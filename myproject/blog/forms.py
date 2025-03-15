from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="name", required=True)
    email = forms.EmailField(label="email", required=True)
    message = forms.CharField(label="message", required=True)


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label="Username", required=True)
    email = forms.EmailField(label="Email", required=True)
    password = forms.CharField(label="Password", required=True, max_length=100)
    confirm_password = forms.CharField(label="Confirm Password", required=True, max_length=100)


    #User model is already defined in django so we are using it. By just importing it and we customize that model by following way.
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        