from django.db import models

# Create your models here.

from django.db import models
import math
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date
from django.utils import timezone

types = (
    ('Type1', 'Type1'),
    ('Type2', 'Type2'),
    ('Type3', 'Type3')
)

#Abstract User
class User(AbstractUser):
    @property
    def is_employee(self):
        if hasattr(self, 'employee'):
            return True
        return False

    @property
    def is_supervisor(self):
        if hasattr(self, 'supervisor'):
            return True
        return False

# Plant Model
class Plant(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Machine Model
class Machine(models.Model):
    machine_number = models.CharField(max_length=200)

    def __str__(self):
        return self.machine_number


# Employee Model
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Supervisor Model
class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

# Downtime Model
class Downtime(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    stoppage_reason = models.CharField(max_length=100)

    def __str__(self):
        return self.stoppage_reason

# Shift Model
class Shift(models.Model):
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=types, blank=False)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.type

# Attendance Model
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    attendance = models.BooleanField(default=False)

    def __str__(self):
        return "Attendance for employee %s: %s" % (self.employee, self.attendance)
