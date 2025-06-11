from django.db import models

# Create your models here.
class Countries(models.Model):
    country_name = models.CharField(max_length=200, null=False, blank=False)
    country_code = models.CharField(max_length=10, null=False, blank=False)
    continent = models.CharField(max_length=20, null=False, blank= False)
    def __str__(self):
        return self.country_name

class Province(models.Model):
    province_name = models.CharField(max_length=200, null=False, blank=False)
    province_cm = models.CharField(max_length=50, null=True, blank=True)
    # district = models.CharField(max_length=20, null=False, blank= False)


