from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('register/', views.register, name='register'),
    path('editUser/', views.password, name='editUser'),
    path('share/', views.share, name='share'),
    path('review/', views.review, name='review'),
    path('history/', views.history, name='history'),
    path('weather/', views.weather, name='weather'),
    path('football/', views.football, name='football'),
    path('time/', views.time, name='time'),
    path('chat_gpt/', views.chatgpt, name='chat_gpt'),
    path('check_username/', views.check, name='check_username'),
    path('check_username2/', views.check2, name='check_username2'),
    path('check_password/', views.pass_check, name='check_password'),
    path('check_password2/', views.pass_check2, name='check_password2'),
    path('email_username/', views.email, name='email_username'),
    path('news/', views.news, name="news"),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('history/<int:history_id>/delete/', views.delete_history, name='delete_history'),

    path('history/clear/', views.clear_history, name='clear_history'),
    path('crypto/', views.crypto, name='crypto'),
    path('cryptocurrency/', views.cryptocurrency, name='cryptocurrency'),
    # reset password urls
    path('password_reset/',auth_views.PasswordResetView.as_view(html_email_template_name='registration/password_reset_email.html'),name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
