from django.db import models

# Create your models here.
class Direcciones(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    direccion_calle_numero = models.TextField()
    direccion_ciudad = models.TextField()
    direccion_provincia = models.TextField()
    direccion_pais = models.TextField()

    class Meta:
        managed = False
        db_table = 'direcciones'

class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()
    direccion = models.OneToOneField(Direcciones, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal'
