from django.db import models

class Flight(models.Model):
    tipo_vuelo = [
        ('N', 'Nacional'),
        ('I', 'Internacional'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255, choices=tipo_vuelo)
    precion = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.type}) - ${self.price}"
