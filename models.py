# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI', unique=True)  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    direccion = models.ForeignKey('Direcciones', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.ForeignKey('TipoCuenta', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'


class Direcciones(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    direccion_calle_numero = models.TextField()
    direccion_ciudad = models.TextField()
    direccion_provincia = models.TextField()
    direccion_pais = models.TextField()

    class Meta:
        managed = False
        db_table = 'direcciones'


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


class MarcaTarjeta(models.Model):
    marca_tarjeta_id = models.AutoField(primary_key=True)
    marca = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'


class Movimientos(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    iban = models.TextField()
    monto = models.IntegerField()
    tipo_operacion = models.TextField()
    hora = models.TextField()

    class Meta:
        managed = False
        db_table = 'movimientos'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()
    direccion = models.OneToOneField(Direcciones, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tarjetas(models.Model):
    tarjeta_id = models.AutoField(primary_key=True)
    numero_tarjeta = models.IntegerField(unique=True)
    cvv = models.IntegerField()
    fecha_emision = models.TextField()
    fecha_vencimiento = models.TextField()
    tipo_tarjeta = models.ForeignKey('TipoTarjeta', models.DO_NOTHING)
    marca_tarjeta = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING)
    account = models.ForeignKey(Cuenta, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tarjetas'


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


class TipoTarjeta(models.Model):
    tipo_tarjeta_id = models.AutoField(primary_key=True)
    tipo_de_tarjeta = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_tarjeta'
