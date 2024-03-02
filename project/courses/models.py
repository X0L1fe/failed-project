from django.db import models
from django.urls import reverse

class Author(models.Model): # автор
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    AuthorEmail = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self) -> str:
        AuthorName = self.FirstName + " " + self.LastName
        return AuthorName

class Course(models.Model): # урок 
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    AuthorEmail = models.EmailField()
    courseName = models.CharField(max_length=120)
    about = models.TextField()
    prices = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    minStudents = models.IntegerField()
    maxStudents = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self) -> str:
        return (self.Author + " " + self.AuthorEmail)

class Student(models.Model): # студент
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Email = models.EmailField()
    password = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)


