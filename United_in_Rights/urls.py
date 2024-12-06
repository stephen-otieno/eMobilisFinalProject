from django.urls import path
from urllib3 import request

from . import views


urlpatterns = [

    path('', views.index, name='home'),
    path('education/', views.education, name='gbv_education'),
    path('clients/', views.clients_list, name='registered_clients'),
    path('view/', views.view_clients, name='registered'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

]