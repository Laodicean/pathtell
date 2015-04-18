from django import forms


class RegisterForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()
    dob = forms.CharField()


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()
