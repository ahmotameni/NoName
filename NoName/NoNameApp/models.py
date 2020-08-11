import datetime

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=10)

    first_name = models.CharField(max_length=20, default=None)
    last_name = models.CharField(max_length=20, default=None)

    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('P', 'Prefer not to say'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    phone_number = models.CharField(max_length=12, default=None, unique=True)
    email = models.EmailField(default=None, unique=True)

    birthday = models.DateTimeField(default=None)

    join_date = models.DateTimeField()


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    followed = models.ForeignKey(User, on_delete=models.CASCADE)

    date = models.DateTimeField()
