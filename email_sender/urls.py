from django.urls import path
from email_sender import views
from email_sender.apps import EmailSenderConfig


app_name = EmailSenderConfig.name

urlpatterns = [
    path('home/', views.base_view, name='home'),
]