from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False) #default - padrão, por padrão está false

    def __str__(self):
        return self.title
