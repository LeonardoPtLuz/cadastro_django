from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    

