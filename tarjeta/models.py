import imp
from django.db import models
from cuenta.models import Cuenta

# Create your models here.

class TipoTarjeta(models.Model):
    tipo_tarjeta_id = models.AutoField(primary_key=True)
    tipo_de_tarjeta = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_tarjeta'
        
class MarcaTarjeta(models.Model):
    marca_tarjeta_id = models.AutoField(primary_key=True)
    marca = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'

class Tarjetas(models.Model):
    tarjeta_id = models.AutoField(primary_key=True)
    numero_tarjeta = models.IntegerField(unique=True)
    cvv = models.IntegerField()
    fecha_emision = models.TextField()
    fecha_vencimiento = models.TextField()
    tipo_tarjeta = models.ForeignKey(TipoTarjeta, models.DO_NOTHING)
    marca_tarjeta = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING)
    account = models.ForeignKey(Cuenta, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tarjetas'
