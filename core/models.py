from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clientes(models.Model):
    nome = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    data_nascimento = models.DateField()
