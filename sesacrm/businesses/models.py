from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CrmUserManager

#Recommended by documentation for future User model customizations
class CrmCustomer(AbstractUser):

	email = models.EmailField(unique=True)
	username = models.CharField(max_length=150, null=True,blank=True)

	USERNAME_FIELD = 'email'

	objects = CrmUserManager() #Custom User Manager to Replace username identifier with email

	REQUIRED_FIELDS = []

	def __str__(self):
		return self.email

# Create your models here.
class Business(models.Model):
	name = models.CharField("Business Name", max_length=100, null=False, blank=False)
	business_type = models.CharField("Business Type", max_length=2, null=False ,blank=False) #Select List
	number = models.IntegerField("Mobile Number", null=False ,blank=False)
	telephone = models.IntegerField("Mobile Number 2", null=True ,blank=True)
	email = models.EmailField("Email", max_length=100,null=False ,blank=False)
	digital_address = models.CharField("Digital Address",max_length=10, null=False ,blank=False)
	business_address = models.CharField("Business Address",max_length=10, null=False ,blank=False)
	business_reg = models.CharField("Digital Registration Number", max_length=10,null=False ,blank=False)
	contact_name = models.CharField("Business Contact Person", max_length=10,null=False ,blank=False)
	tin = models.CharField("Tax Identification Number", max_length=10,null=False ,blank=False)
	approved = models.BooleanField("Approved?", default=False)


	def __str__(self):
		return self.name