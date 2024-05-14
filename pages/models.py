# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adquiere(models.Model):
    id_producto = models.OneToOneField('Producto', models.DO_NOTHING, db_column='id_Producto', primary_key=True)  # Field name made lowercase. The composite primary key (id_Producto, id_cliente) found, that is not supported. The first column is selected.
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente')
    cantidad_productos = models.IntegerField()
    fecha_adq = models.DateField()

    class Meta:
        managed = False
        db_table = 'adquiere'
        unique_together = (('id_producto', 'id_cliente'),)


class Asociado(models.Model):
    id_registro = models.OneToOneField('Registrocompra', models.DO_NOTHING, db_column='id_registro', primary_key=True)  # The composite primary key (id_registro, id_compra) found, that is not supported. The first column is selected.
    id_compra = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_compra')

    class Meta:
        managed = False
        db_table = 'asociado'
        unique_together = (('id_registro', 'id_compra'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=10)  # The composite primary key (id_cliente, id_compra) found, that is not supported. The first column is selected.
    nombre_cliente = models.CharField(max_length=45)
    direccion = models.CharField(max_length=55, blank=True, null=True)
    id_compra = models.OneToOneField('Venta', models.DO_NOTHING, db_column='id_compra')

    class Meta:
        managed = False
        db_table = 'cliente'
        unique_together = (('id_cliente', 'id_compra'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fiados(models.Model):
    nombre_cliente = models.CharField(primary_key=True, max_length=45)  # The composite primary key (nombre_cliente, id_cliente) found, that is not supported. The first column is selected.
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    deuda_total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'fiados'
        unique_together = (('nombre_cliente', 'id_cliente'),)


class Inventario(models.Model):
    tipo_producto = models.CharField(primary_key=True, max_length=10)  # The composite primary key (tipo_producto, id_producto) found, that is not supported. The first column is selected.
    cantidad_productos = models.IntegerField()
    id_producto = models.OneToOneField('Producto', models.DO_NOTHING, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'inventario'
        unique_together = (('tipo_producto', 'id_producto'),)


class Producto(models.Model):
    id_producto = models.CharField(db_column='id_Producto', primary_key=True, max_length=15)  # Field name made lowercase.
    nombre_producto = models.CharField(max_length=25)
    precio_venta = models.FloatField()
    tipo_de_movimiento = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.CharField(db_column='id_Proveedor', primary_key=True, max_length=10)  # Field name made lowercase.
    producto_entrega = models.CharField(max_length=30)
    nombre_proveedor = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Registrocompra(models.Model):
    id_registro = models.CharField(primary_key=True, max_length=15)
    precio_compra = models.FloatField()
    tipo_pago = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'registrocompra'


class Suministra(models.Model):
    id_producto = models.OneToOneField(Producto, models.DO_NOTHING, db_column='id_Producto', primary_key=True)  # Field name made lowercase. The composite primary key (id_Producto, id_Proveedor) found, that is not supported. The first column is selected.
    id_proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='id_Proveedor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'suministra'
        unique_together = (('id_producto', 'id_proveedor'),)


class Venta(models.Model):
    id_compra = models.CharField(primary_key=True, max_length=15)  # The composite primary key (id_compra, id_Producto) found, that is not supported. The first column is selected.
    fecha = models.DateField()
    precio_compra = models.FloatField()
    id_producto = models.OneToOneField(Producto, models.DO_NOTHING, db_column='id_Producto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venta'
        unique_together = (('id_compra', 'id_producto'),)
