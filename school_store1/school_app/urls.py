from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/',views.register,name='register'),
    path('new/',views.new_page,name='new'),
    path('form/',views.form,name='form'),
    path('message/',views.msg,name='msg'),
    path('navdrop/',views.navdrop,name='nav'),
    # Add more URL patterns as needed
]
