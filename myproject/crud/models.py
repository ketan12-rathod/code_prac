from django.db import models

# Create your models here.
class login(models.Model):
    name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    contact=models.BigIntegerField()

    class Meta:
        db_table='login'
        

        
