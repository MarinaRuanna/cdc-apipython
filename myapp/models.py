from django.db import models


class Autor(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    descricao = models.CharField(max_length=400)

    def __str__(self):
        return self.name
