from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'dob', 'photo', 'level', 'gender', 'department', 'bio', 'matric_no', 
					'staff_id', 'verified_student', 'verified_staff']
