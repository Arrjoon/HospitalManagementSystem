from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('base/', views.base, name="base"),
    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('admin_login/', views.login, name="login"),
    path('admin_logout/', views.logout_admin, name="logout"),
    path('view_doctor/', views.view_doctor, name="view_doctor"),
    path('delete_doctor(?P<int:pid>)/',
         views.delete_doctor, name="delete_doctor"),
    path('add_doctor/', views.Add_doctor, name="add_doctor"),

    path('view_patient/', views.view_patient, name="view_patient"),
    path('add_patient/', views.add_patient, name="add_patient"),
    path('delete_patient(?P<int:pid>)/',
         views.delete_doctor, name="delete_patient"),

    path('view_appointment/', views.view_appointment, name="view_appointment"),
    path('add_appointment/', views.add_appointment, name="add_appointment"),
    #     path('delete_appointment(?P<int:pid>)/',
    #          views.delete_appointment, name="delete_appointment"),
]
