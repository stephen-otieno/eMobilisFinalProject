from django.urls import path
from urllib3 import request

from . import views


urlpatterns = [

    path('', views.index, name='home'),
    path('education/', views.education, name='gbv_education'),
    path('clients/', views.victims_list, name='registered_clients'),
    path('victims/', views.view_victims, name='abused_victims'),
    path('report/', views.report, name='report_abuse'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('registered/', views.clients_list, name='registered'),


]