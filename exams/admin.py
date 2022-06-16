from django.contrib import admin
from .models import Exam, User

# Register your models here.
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
	list_display = ['poster', 'room', 'course_title', 'course_code', 'invigilator', 'completed', 'exam_date']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'first_name', 'last_name', 'email', 'account_type', 'date_created']
