from .import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('start', views.start, name='start'),
    path('form', views.form, name='form'),
    path('final',views.final, name='final'),
]