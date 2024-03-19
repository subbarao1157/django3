from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100,blank=False)
    course=models.CharField(max_length=100,blank=False)
    fees=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student'