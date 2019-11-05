from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Plant,Machine, Employee, Supervisor, Downtime, Shift, Attendance
from django.contrib.auth.admin import UserAdmin



admin.site.register(User, UserAdmin)
admin.site.register(Plant)
admin.site.register(Machine)
admin.site.register(Employee)
admin.site.register(Supervisor)
admin.site.register(Downtime)
admin.site.register(Shift)
admin.site.register(Attendance)