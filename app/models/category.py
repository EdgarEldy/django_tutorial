from django.db import models

# Category model
class Category(models.Model):
    cat_name = models.CharField(max_length=45)

    def __str__(self):
        return self.cat_name