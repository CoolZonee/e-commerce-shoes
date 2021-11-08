from django.db import models
from django.contrib.auth.models import AbstractUser


class Position(models.Model):
    name = models.CharField(max_length=50)
    job_desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = None
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    email = models.EmailField(unique=True, blank=False, null=False)
    mobile_no = models.CharField(
        max_length=20, unique=True, blank=False, null=False)
    dob = models.DateField(default=None)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    joined_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
