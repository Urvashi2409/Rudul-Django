from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)  # need to mention max_length here 
    attendance = models.CharField(max_length=50)
    isgood = models.BooleanField(default=False)

    def __str__(self):
        return self.student_id + " has name " + self.name
