from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    end = models.BooleanField()
    task = models.CharField(max_length=100)
    limit = models.DateField()
    memo = models.CharField(max_length=500)

    def multi_return(self):
        return self.task, self.limit, self.end

    def __str__(self):
        return str(self.limit) + self.task