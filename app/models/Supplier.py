from django.db import models

#Supplier Model
class Supplier(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    tel = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    address = models.CharField(max_length=45)

#Get supplier's first_name and last_name 
    def __str__(self):
        return self.first_name + ' ' + self.last_name