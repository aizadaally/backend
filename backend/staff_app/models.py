from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.db import models

class Department(models.Model):
    role = models.CharField(max_length=128)

    def __str__(self):
        return self.role
    

class Staff(models.Model):
    name = models.CharField(max_length=128,null=False, blank=False, verbose_name="Name")
    phone_number = PhoneNumberField(blank=True,null=True,unique=True, verbose_name="Phone Number")
    # created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Created At")
    email = models.EmailField(max_length=128, null=False, blank=False, verbose_name="Gmail", unique=True )
    gender = models.CharField(max_length=10 ,choices=[('Male', 'Male'), ('Female', 'Female')], verbose_name="Gender")
    department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    # is_staff = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)
    # is_superadmin = models.BooleanField(default=False)

    def str(self):
        return self.name


class Record(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT, verbose_name="Staff")
    datetime = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name="Time")
    action = models.CharField(max_length=100, choices=[("in", 'In'), ('out', 'Out')])

    # made_by = models.ForeignKey(Staff, on_delete=models.PROTECT, blank=True, null=True, related_name="security")