from django.db import models

# Profile model
class Profile(models.Model):
    profile_name = models.CharField(max_length=45)

    def __str__(self):
        return self.profile_name