from django import forms
from .models import *

class AddCourseForm(forms.ModelForm):
    # class Meta:
    #     model = Course
    #     fields = '__all__'
    Author = forms.CharField(max_length=50)
    AuthorEmail = forms.EmailField()
    courseName = forms.CharField(max_length=120)
    about = forms.CharField()
    prices = forms.BooleanField()
    price = forms.DecimalField(max_digits=10000, decimal_places=2)
    minStudents = forms.IntegerField()
    maxStudents = forms.IntegerField()
    startDate = forms.DateField()
    endDate = forms.DateField()




