from django import forms


class AddPersonServiceConnectionForm(forms.Form):
    service_id = forms.CharField()
