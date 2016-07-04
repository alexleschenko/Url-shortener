from django import forms

class URL_create(forms.Form):
    url = forms.URLField(label='Url', max_length=200)