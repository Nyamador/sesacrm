from django.db import models
from businesses.models import Business

gender_list = (
    ('m', 'Male'),
    ('f', 'Female'),
)

# Create your models here.
class Customer(models.Model):
	"""
	Model for customer to be added by business owner
	"""
	name = models.CharField("Customer Name", max_length=200,null=False,blank=False)
	number = models.IntegerField("Telephone Number",null=False,blank=False)
	phone = models.IntegerField("Telephone 2", null=True,blank=True)
	sex = models.CharField("Gender", max_length=1, blank=False, null=False, choices=gender_list, help_text="Gender")
	location  = models.CharField("Location",max_length=100)
	birth_date = models.DateField("Date of Birth",auto_now=False, auto_now_add=False)
	business = models.ForeignKey(Business, on_delete=models.CASCADE)
	#Name of the business which registers the customer

	def __str__(self):
		return self.name


