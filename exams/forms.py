from django import forms
from .models import Exam

class ExamForm(forms.ModelForm):
	class Meta:
		model = Exam
		fields = ('course_title','course_code','invigilator','room', 'description', 'completed', 'exam_date')
		exclude = ('poster',)
