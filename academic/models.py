from django.db import models

class Curso(models.Model):
    name = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()
