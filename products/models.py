from django.db import models
from django.db import models

# Create your models here.


class Product(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)  # ex: 199.99

    def __str__(self):
        return f"{self.nom} - {self.prix} €"
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

