from django.db import models

# Create your models here.

class Todoapp(models.Model):
    task_description = models.TextField()
    


