from django.db import models
from cliente.models import Direcciones, Cliente

# Create your models here.
class AuditoriaCuenta(models.Model):
    id_auditoria_cuenta = models.AutoField(primary_key=True)
    old_id = models.IntegerField()
    new_id = models.IntegerField()
    old_balance = models.IntegerField()
    new_balance = models.IntegerField()
    old_iban = models.TextField()
    new_iban = models.TextField()
    old_type = models.TextField()
    new_type = models.TextField()
    user_action = models.TextField()
    created_at = models.TextField()

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'

class TipoCliente(models.Model):
    tipo_cliente_id = models.AutoField(primary_key=True)
    tipo_cliente_nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente'

class TipoCuenta(models.Model):
    tipo_cuenta_id = models.AutoField(db_column='tipo_cuenta_Id', primary_key=True)  # Field name made lowercase.
    cuenta_corriente = models.IntegerField()
    caja_ahorro_pesos = models.IntegerField()
    caja_ahorro_dolares = models.IntegerField()
    tipo_cliente = models.ForeignKey(TipoCliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.ForeignKey(TipoCuenta, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()
    direccion = models.ForeignKey(Direcciones, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'

class Movimientos(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    iban = models.TextField()
    monto = models.IntegerField()
    tipo_operacion = models.TextField()
    hora = models.TextField()

    class Meta:
        managed = False
        db_table = 'movimientos'
