from django.db import models

class Veiculo(models.Model):
      tipo = models.Charfield(max_length=50)
      nome = models.Charfield(max_length=50)
      ano = models.Integerfield(max_length=4)
      fabricante = models.Charfield(max_length=50)



