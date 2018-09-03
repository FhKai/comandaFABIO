from django.db import models

class Restaurante(models.Model):
    nome = models.CharField(max_length=50)
    slug = models.SlugField()
    descricao = models.CharField(max_length=255)
#    foto = models.FileField(upload_to='static/restaurante/fotosRestaurante/')
    endereco = models.CharField(max_length=140)
    cozinha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

# Create your models here.
