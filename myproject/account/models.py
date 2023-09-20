from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Profile(models.Model):
    contact = models.BigIntegerField()
    address = models.TextField()
    user    = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'profile'

class Feedback(models.Model):
    rating = models.CharField(max_length=10)
    comment = models.TextField()
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    date    = models.DateField(default=date.today)

    class Meta:
        db_table = 'feedback'