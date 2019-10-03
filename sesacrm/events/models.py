from django.db import models

# Create your models here.
class event(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)
  event_type = models.CharField(max_length=100, null=False, blank=False,help_text="Birthday ,  Holiday...")
  event_message = models.CharField(max_length=100, null=False, blank=False, help_text="Dear Customer....")