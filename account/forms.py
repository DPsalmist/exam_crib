from django import forms
#from django.contrib.auth.models import User
from .models import Profile
from exams.models import User

class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')
		print('user is', User.account_type)
		#fields = '__all__'
		#exclude = ('account_type', '')


class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('dob', 'bio', 'gender', 'phone_no', 'nationality', 'department')
		def __init__(self, *args, **kwargs):
			super(ProfileEditForm, self).__init__(*args, **kwargs)
			if Profile.verified_staff == True and Profile.verified_student == False:
				exclude = ('matric_no',)
			elif Profile.verified_student == True and Profile.verified_staff == False:
				exclude = ('matric_no',)

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', 
								widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password',
								widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'account_type', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('passwords don\'t match!')
		return cd['password2']

class LoginForm(forms.Form):
	username = forms.CharField(label='Enter your username')
	password = forms.CharField(label='Enter your password', widget=forms.PasswordInput)