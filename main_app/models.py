from django.db import models

class Budget(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# Create your models here.
