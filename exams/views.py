from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Exam
from account.models import User
from django.views.generic import ( ListView, DetailView, CreateView, UpdateView, DeleteView )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

# Create your views here.
class ExamListView(ListView):
	model = Exam
	template_name = 'exams/exam_list.html' 
	context_object_name = 'all_exams'
	ordering = ['-created'] 
	paginate_by = 3

	def get_context_data(self, **kwargs):
		pending_exams = Exam.objects.filter(completed=False)
		pending_exams = pending_exams.count()
		print('pending_exams', pending_exams)
		context = {'pending_exams':pending_exams}
		kwargs.update(context)
		return super().get_context_data(**kwargs)


class UserExamListView(ListView):
	model = Exam
	template_name = 'exams/user_exams.html' 
	context_object_name = 'my_exams'
	ordering = ['-created'] 
	paginate_by = 3

	def get_queryset(self):
		#getting the username from the url 
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		print('this user:', user)
		return Exam.objects.filter(poster=user).order_by('-exam_date')

	def get_context_data(self, **kwargs):
		pending_exams = Exam.objects.filter(completed=False)
		pending_exams = pending_exams.count()
		print('pending_exams', pending_exams)
		context = {'pending_exams':pending_exams}
		kwargs.update(context)
		return super().get_context_data(**kwargs)

class ExamCreateView(LoginRequiredMixin, CreateView):
	model = Exam
	fields = '__all__'
	exclude = ['poster', 'created']

	#overriding the form valid method
	def form_valid(self, form):
		form.instance.owner  = self.request.user
		return super().form_valid(form)

class ExamUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Exam
	fields = '__all__'
	exclude = ['poster', 'created']
	
	def form_valid(self, form):
		form.instance.poster  = self.request.user
		return super().form_valid(form)

	#test function to make only an authorised user update a photo
	def test_func(self):
		exam = self.get_object()
		if self.request.user == exam.poster:
			return True
		return False

class ExamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Exam
	success_url = '/'

	#test function to make only an authorised user delete a post
	def test_func(self):
		exam = self.get_object()
		if self.request.user == exam.poster:
			return True
		return False


#function detailview
def viewExam(request, pk):
	exam = get_object_or_404(Exam, id=pk)
	user = request.user
	pending_exams = Exam.objects.filter(completed=False)
	pending_exams = pending_exams.count()

	context = {
		'exam':exam,
		'user':user,
		'pending_exams':pending_exams,
    }
	return render(request, 'exams/exam_detail.html', context)