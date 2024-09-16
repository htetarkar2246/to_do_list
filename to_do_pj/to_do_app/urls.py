from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home-page'),
    path('register',views.register, name='register-page'),
    path('login',views.login, name='login-page'),
    path('logout/', views.logout, name='logout'),
    path('delete-task/<str:name>', views.deleteTask, name='delete'),
    path('update/<str:name>', views.update, name='update')
]