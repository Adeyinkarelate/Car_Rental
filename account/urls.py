from django.urls import path
from  .views import register ,user_login , logout , edit_profile
from django.contrib.auth import views


urlpatterns = [
    path('', register , name='register'),
    path('login/', user_login , name='login'),
    path('logout/', logout , name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('password_reset/',views.PasswordResetView.as_view(template_name='account/password_reset.html'), name="password-reset"),
    path('password_reset_done/',views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset_complete/',views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),name="password_reset_complete"),
    
    
  
]