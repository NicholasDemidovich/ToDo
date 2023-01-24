from django.db import models

# Create your models here.

class ToDo(models.Model):
    Title = models.CharField('Task name', max_length= 200, blank=False)
    Description = models.TextField(blank=True)
    Date = models.DateField(blank=False)
    Completed = models.BooleanField(default=False)

    def __str__(self):
        return self.Title