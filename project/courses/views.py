from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import AddCourseForm
from .models import *

# Create your views here.



def index(request):
    menu = [
        {'title': 'О нас', 'url_name':'about'},
        {'title': 'Войти', 'url_name': 'login'},
        {'title': 'Добавить курс', 'url_name': 'addcourse'}
    ]
    return render(request, 'courses/index.html', {'menu': menu})

def list_course(request):
    posts = Author.objects.all()
    return render(request, 'courses/list_courses.html', {'posts': posts})

def addcourse(request):
    form = AddCourseForm()
    return render(request, 'courses/Add_Courses.html', {'form': form})

def about(request):
    return render(request, 'courses/about.html')

def login(request):
    return render(request, 'courses/login.html')



def pageNotFound(request, exception):
    return render(request, 'courses/404.html')