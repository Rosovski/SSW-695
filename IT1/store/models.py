from django.db import models
# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=120)
    business_name = models.CharField(max_length=250)
    mobile = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    street_address = models.CharField(max_length=250)
    street_address_2 = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=20, default='United States')
    business_type = models.CharField(max_length=20)
    registration_date = models.DateField()
