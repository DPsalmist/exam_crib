from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
	account = (
			('select account', 'select account'),
			('student', 'student'),
			('staff', 'staff')
		)
	account_type = models.CharField(max_length=200, choices=account, default='select account')
	email = models.CharField(max_length = 200, blank=True, unique=True)
	first_name = models.CharField(max_length=200, blank=True)
	last_name = models.CharField(max_length=200, blank=True)
	username = models.CharField(max_length = 200, blank=True, unique=True)
	date_created = models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	def __str__(self):
		return self.username

class Exam(models.Model):
	course_title = models.CharField(max_length=200, blank=True)
	course_code =  models.CharField(max_length=200, blank=True)
	invigilator = models.CharField(max_length=200, blank=True)
	room = models.CharField(max_length=100, blank=True, default='')
	completed = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	description = models.TextField(blank=True)
	exam_date = models.DateTimeField(auto_now=True)
	poster = models.ForeignKey(User, blank=True, related_name='exams', on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['created']

	def __str__(self):
		return self.course_title

	def get_absolute_url(self):
		return reverse('exams:exam-list')