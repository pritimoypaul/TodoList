from django.db import models

# Create your models here.


class todos(models.Model):
    todoName = models.CharField(max_length=124)
    description = models.TextField(max_length=None)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.todoName
