from django import forms
from django.contrib.auth import models

from .models import *


class NewPaperForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control'}))
    school = forms.CharField(label='School', widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control'}))
    description = forms.CharField(label='description', widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control'}))
    website = forms.URLField(label='Website URL', widget=forms.URLInput(
            attrs={'class': 'form-control'}))
    city = forms.CharField(label='City', max_length=240, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control'}))
    state = forms.CharField(label='State', max_length=2, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control'}))


    def __init__(self, *args, **kwargs):
        super(NewPaperForm, self).__init__(*args, **kwargs)


    def save(self, commit=True):
        paper = Paper(
            name=self.cleaned_data['name'],
            school=self.cleaned_data['school'],
            description=self.cleaned_data['description'],
            website=self.cleaned_data['website'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
        )

        return paper
