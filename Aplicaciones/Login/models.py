from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    correo = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)