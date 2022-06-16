from django.urls import path
from . import views 
from .views import (
 ExamListView, 
 #ExamDetailView,
 ExamCreateView,
 ExamUpdateView,
 ExamDeleteView,
 UserExamListView,
 )

app_name = 'exams'

urlpatterns = [
    path('exams/', ExamListView.as_view(), name='exam-list'),
    path('exam/<str:pk>/', views.viewExam, name='exam_detail'),
    path('user/<str:username>', UserExamListView.as_view(), name='user_exams'),
    #path('exam/<int:pk>/', ExamDetailView.as_view(), name='photo_detail'),
    path('exam/<int:pk>/update', ExamUpdateView.as_view(), name='exam-update'),
    path('exam/<int:pk>/delete', ExamDeleteView.as_view(), name='exam-delete'),
    path('add/new/', ExamCreateView.as_view(), name='add'),
]