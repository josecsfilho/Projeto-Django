
from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


class Projeto(models.Model):
    título = CharField(max_length=100)
    descrição = CharField(max_length=250)
    imagem = ImageField(upload_to='portifolio/imagens/')    
    url = URLField(blank=True)
