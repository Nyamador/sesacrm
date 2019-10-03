from django.db import models
from customers.models import Customer

delivery_method( ('mail','E-mail'), ('sms', 'sms'))
# Create your models here.
class message(models.Model):
	to = models.ForeignKey(Customer, on_delete=models.CASCADE)
	delivery = models.CharField(max_length=5, choices=delivery_method)
	title = models.CharField(max_length=100, null=False, blank=False)
	body = models.CharField(max_length=200,null=False, blank=False)