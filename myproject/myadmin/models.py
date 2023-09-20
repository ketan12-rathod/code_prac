from django.db import models

# Create your models here.
class Register(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    contact=models.BigIntegerField()

    class Meta:
        db_table='register'
        
class Employee(models.Model):
    e_name=models.CharField(max_length=30)
    def __str__(self):
        return self.e_name
    class Meta:
        db_table='employee'
        
class Sallary(models.Model):
    sallary=models.DecimalField(max_digits=10,decimal_places=2)
    employee=models.OneToOneField(Employee,on_delete=models.CASCADE)

    class Meta:
        db_table='sallary'
        
