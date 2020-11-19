from django import forms
from django.forms import ModelForm

from .models import Inquiries, MembersOfProgram



class InquiriesForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {'placeholder':'Your name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs = {'placeholder':'Email Address'}))
    message = forms.CharField(widget=forms.Textarea(attrs = {}))

    class Meta:
        model = Inquiries
        fields = '__all__'

class MembersOfProgramForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {'placeholder':'First name'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {'placeholder':'Last name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs = {'placeholder':'Email Address'}))
    phone_number = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {'placeholder':'Phone number'}))

    class Meta:
        model = MembersOfProgram
        fields = '__all__'
