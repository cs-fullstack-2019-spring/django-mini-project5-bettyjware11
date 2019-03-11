from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class RecipeModel(models.Model):
    shortDescription = models.CharField(max_length=200, default="")
    ingredients = models.CharField(max_length=800, default="")
    directions = models.CharField(max_length=1000, default= "")
    nameOfMeal = models.CharField(max_length=200, default="")
    mealPicture = models.CharField(max_length=800, default="")
    dateCreated = models.DateField(default= timezone.now)
    foreignkeyToUser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return "The recipe name is: " + str(self.nameOfMeal)


class UserModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    password1 = models.CharField(max_length=200, default="")
    password2 = models.CharField(max_length=200, default="")
    profilePicture = models.CharField(max_length=800, default="")
    emailAddress = models.EmailField

    def __str__(self):
        return "This meal was created by: " + str(self.username)