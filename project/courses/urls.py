from django.urls import path

from .views import *

urlpatterns = [
    path('home/', index, name='home'),
    path('courses/', list_course, name='courses'),
    path('courses/add/', addcourse, name='addcourse'),
    path('login', login, name='login'),
    path('about', about, name='about'),
]

