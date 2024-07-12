from django.db import models

# Create your models here.

class Visitor(models.Model):
    Key = models.CharField(max_length=100,null=True)