from django.db import models

# Create your models here.

class put_data(models.Model):
    column_one = models.CharField(max_length=140)
    column_two = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.column_one
