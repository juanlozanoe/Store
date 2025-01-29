from django.db import models
from django.utils import timezone

# Create your models here.
class Marca(models.Model):
    """ Modelo que permite registrar las marcas de los productos"""

    categorias_list = (
        ('1', 'Pantalones'),
        ('2', 'Calzado'),
        ('3', 'Joyeria'),
        ('4', 'Perfumeria'),
        ('5', 'Camisas'),
        ('6', 'Camisetas'),
        ('7', 'blusas'),
    )

    nombre = models.CharField(max_length=200, null=False, blank=False)
    categorias = models.CharField(max_length=200, choices=categorias_list, null=False, blank=False)
    descripcion = models.CharField(max_length=200, null=False, blank=False)
    estado = models.BooleanField(default=True)
    created_at =models.DateTimeField(default=timezone.now)
    updated_at =models.DateTimeField(null=True, blank=True)
    deleted_at =models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return str(f"ID {self.id} Nombre {self.nombre}")