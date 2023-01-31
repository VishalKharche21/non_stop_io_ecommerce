from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    Pname = models.CharField(max_length=100)
    Shape = models.CharField(max_length=50)
    Size = models.CharField(max_length=50)
    location = models.CharField(max_length=200,blank=True,null=True)
    price = models.IntegerField()

class Signup(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    age=models.IntegerField()
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

