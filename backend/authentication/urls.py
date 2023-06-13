from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('student/', views.getStudent, name="student info"),
    path('teacher/', views.getTeacher, name="student info")
]

