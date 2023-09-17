from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username}: {self.email}"


class History(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateField(auto_now=True)
