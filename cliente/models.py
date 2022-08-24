from django.db import models
from sucursal.models import Sucursal, Direcciones


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI', unique=True)  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.ForeignKey(Sucursal, models.DO_NOTHING, blank=True, null=True)
    direccion = models.ForeignKey(Direcciones, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self) -> str:
        return self.customer_name