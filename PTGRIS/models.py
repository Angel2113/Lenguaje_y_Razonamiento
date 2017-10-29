from django.db import models

# Create your models here.
class Tweet(models.Model):
    text = models.CharField(max_length=160, null=True, blank=True)
    busqueda = models.ForeignKey('Busqueda', on_delete=models.CASCADE, null=True, blank=True)
    ide = models.CharField(max_length=255, null=True, blank=True)
    permalink = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    text = models.CharField(max_length=255, null=True, blank=True)
    date = models.CharField(max_length=255, null=True, blank=True)
    formatted_date = models.CharField(max_length=255, null=True, blank=True)
    retweets = models.CharField(max_length=255, null=True, blank=True)
    favorites = models.CharField(max_length=255, null=True, blank=True)
    mentions = models.CharField(max_length=255, null=True, blank=True)
    hashtags = models.CharField(max_length=255, null=True, blank=True)
    geo = models.CharField(max_length=255, null=True, blank=True)
    urls = models.CharField(max_length=255, null=True, blank=True)
    author_id = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.text

class Busqueda(models.Model):
    busqueda = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.busqueda
