from django.db import models
#from django.contrib.auth.models import AbstractUser
from exams.models import User

# Create your models here.

class Profile(models.Model):
	gender = (
			('select', 'select'),
			('male', 'male'),
			('female', 'female')
		)
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	dob = models.DateField(blank=True, null=True)
	bio = models.CharField(max_length=200, blank=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d', default='media/default.jpeg', blank=True)
	level = models.CharField(max_length=200, blank=True, default=100)
	gender = models.CharField(max_length=100, choices=gender, default='select')
	department = models.CharField(max_length=200, blank=True)
	nationality = models.CharField(max_length=100, blank=True, default='Nigeria')
	phone_no = models.CharField(max_length=100, blank=True)
	matric_no = models.CharField(max_length=100, blank=True, null=True)
	staff_id = models.CharField(max_length=100, blank=True, null=True)
	verified_student = models.BooleanField(default=False)
	verified_staff = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)