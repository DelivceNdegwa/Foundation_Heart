from django import forms
from django.forms import ModelForm

from .models import Inquiries, MembersOfProgram



class InquiriesForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {'placeholder':'Your name', 'class':'form-control-custom mb-4'}))
    email = forms.EmailField(widget=forms.TextInput(attrs = {'placeholder':'Email Address', 'class':'form-control-custom mb-4'}))
    message = forms.CharField(widget=forms.Textarea(attrs = {'placeholder':'Your Message', 'class':'form-control-custom mb-4', 'rows':'3'}))

    class Meta:
        model = Inquiries
        fields = '__all__'

class MembersOfProgramForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {'placeholder':'First name', 'class':'form-control-custom mb-4'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {'placeholder':'Last name', 'class':'form-control-custom mb-4'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs = {'placeholder':'Email Address', 'class':'form-control-custom mb-4'}))
    phone_number = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {'placeholder':'Phone number', 'class':'form-control-custom mb-4'}))

    class Meta:
        model = MembersOfProgram
        fields = '__all__'
