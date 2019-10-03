from django import forms
from .models import Business

class BusinessRegistrationForm(forms.ModelForm):

  class Meta:
    model = Business
    fields = ['name', 'business_type' , 'number' ,'telephone', 'email' , 'digital_address' , 'business_address', 'business_reg' , 'contact_name', 'tin']