from django.db import models

from Sprint_8.HomeBanking.cliente.models import Cliente
from cliente.models import Cliente

# Create your models here.

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prestamo'