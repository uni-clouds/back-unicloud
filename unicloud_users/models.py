from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class UserPreferencesModel(models.Model):
    language = models.CharField(max_length=2, null=True)
    theme = models.CharField(max_length=10, null=True)
    user = models.OneToOneField(User, related_name='userpreference', on_delete=models.CASCADE)