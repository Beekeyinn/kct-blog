from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to="profiles")
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
