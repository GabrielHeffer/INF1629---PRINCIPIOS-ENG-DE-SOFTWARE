from django.db import models

class Request(models.Model):
    nome = models.CharField('Nome', max_length=100)
    urlBase = models.CharField('urlBase', max_length=200)
    OBdata = models.CharField('OBdata', max_length=50)
    OBrelevancia = models.CharField('OBrelevancia', max_length=50)
