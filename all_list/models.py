from django.db import models

class ToDo(models.Model):
    end = models.BooleanField()
    task = models.CharField(max_length=100)
    limit = models.DateField()
    memo = models.CharField(max_length=500)

    def multi_return(self):
        return self.task, self.limit, self.end