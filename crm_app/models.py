from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField(max_length=1200)
    create_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.name
