from pyclbr import Class
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null = True,   blank=True)
    First_name = models.CharField(max_length=10,null = True)
    last_name = models.CharField(max_length=10,null = True)
    emp_image = models.ImageField(upload_to='empimg',null = True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    hire_date = models.DateField(null=True, blank=True)
    recipe_view_count = models.IntegerField(default=1)
    
                    
  
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department
    
    class Meta:
        ordering =['department']

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self):
        return self.student_id

class Student(models.Model):
    department = models.ForeignKey(Department,on_delete =models.CASCADE, related_name="depart")
    student_id = models.OneToOneField(StudentID,on_delete=models.CASCADE,related_name="studentid")
    student_name = models.CharField(max_length=100)
    student_email= models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()


    def __str__(self):
        return self.student_name
    

    class Meta:
        ordering =['student_name']