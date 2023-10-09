from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age=models.IntegerField()
    gender = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(max_length=250)
    district = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)
    materials_req = models.CharField(max_length=50)
    def __str__(self):
        return self.name