from django.urls import path
from . import views
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('password-reset/', PasswordResetView.as_view(template_name='userapp/password_reset.html'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='userapp/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='userapp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='userapp/password_reset_complete.html'), name='password_reset_complete'),
]
