from django.db import models


class Auto(models.Model):
    """Model de base de datos de un Auto."""
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    chapa = models.CharField(max_length=9)
    creado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['creado']
        
    def __str__(self):
        return f'Marca: {self.marca}, ID: {self.id}'
        

    