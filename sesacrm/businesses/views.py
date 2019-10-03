from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import BusinessRegistrationForm
import smtplib
from email.mime.text import MIMEText

# Create your views here.
def index(request):

  return render(request, 'businesses/index.html')


def register(request):
  if request.method == 'POST':
    form = BusinessRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      name = form.cleaned_data.get('name')      
      messages.success(request, f'You have successfully requested for a business account - {name}')
      return redirect ('home-view')      
  else:
      form = BusinessRegistrationForm()    
  return render(request, 'businesses/business-registration.html',{'form' : form})