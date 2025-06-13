from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=25, null=False, blank=False, unique=True)
    phone_no = models.IntegerField(max_length=10, null=False, blank=False)
    contact_date = models.DateTimeField(default=datetime.now())
    address = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(max_length=250,null=False,  blank=False)

    def __str__(self):
        return self.first_name