from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords does not match')


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100, required=True)
    password = forms.CharField(label='password', max_length=100, required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password")