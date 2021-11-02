from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=50)
    job_desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=20)
    dob = models.DateField(default=None)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    joined_date = models.DateTimeField(auto_now_add=True)
