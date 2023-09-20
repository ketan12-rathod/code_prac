from django.contrib import admin
from myadmin.models import Register,Employee,Sallary
# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','contact']
    search_fields=['contact']

admin.site.register(Register,RegisterAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['e_name']

admin.site.register(Employee,EmployeeAdmin)

class SallaryAdmin(admin.ModelAdmin):
    list_display=['sallary']

admin.site.register(Sallary,SallaryAdmin)