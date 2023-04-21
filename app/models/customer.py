from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    telephone = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name