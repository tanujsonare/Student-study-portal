from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Subject(models.Model):
    subject = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.subject}"

class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    status_choice = (
        ("Incomplete","Incomplete"),("Completed","Completed")
        )
    status = models.CharField(max_length=20,choices=status_choice,default='Incomplete')

    def __str__(self):
        return f"{self.title}"


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    todo_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"


        