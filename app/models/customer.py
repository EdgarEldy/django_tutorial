from django.db import models

# Customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    tel = models.CharField(max_length=45)
    address = models.CharField(max_length=45)

    def __str__(self):
        return self.first_name + ' ' + self.last_name