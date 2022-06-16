from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	# registration route
	path('register/', views.register, name='register'),
	# login routes
	#path('login/', views.user_login, name='login'),
	path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
	# edit
	path('edit/', views.edit, name='edit'),
	# dashboard
	path('', views.dashboard, name='dashboard'),

	#password_change
	path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	#reset password urls
	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]