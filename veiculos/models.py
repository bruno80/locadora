from django.db import models

class Veiculo(models.Model):
      tipo = models.CharField(max_length=50)
      nome = models.CharField(max_length=50)
      ano = models.CharField(max_length=4)
      fabricante = models.CharField(max_length=50)



