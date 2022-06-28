from django.db import models


class Hidrometrica(models.Model):
    fecha = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'Hidrometrica'
        ordering = ['-fecha']
    
    def __str__(self):
        return f'Fecha: {self.fecha} - Nivel: {self.nivel}'
      