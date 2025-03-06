from django.db import models

# Create your models here.
class Student(models.Model):
    StudentID = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dateofbirth = models.DateField()
    course = models.CharField(max_length=100)
    enrollmentdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
