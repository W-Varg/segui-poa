from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cargo(models.Model):
    idcargo = models.AutoField(primary_key=True)
    nombrecargo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargo'


class Persona(models.Model):
    idpersona = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=250, blank=True, null=True)
    apellido1 = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    celular = models.CharField(max_length=25, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persona'

class Unidad(models.Model):
    idunidad = models.AutoField(primary_key=True)
    secretaria = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    estado = models.NullBooleanField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    codunidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidad'

class Usuarios(models.Model):
    idusuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    creacion = models.DateField(blank=True, null=True)
    idunidad = models.ForeignKey(Unidad, models.DO_NOTHING, db_column='idunidad', blank=True, null=True)
    idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='idpersona', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'

class Gestion(models.Model):
    idgestion = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=8, blank=True, null=True)
    observacion = models.CharField(max_length=50, blank=True, null=True)
    inicio = models.DateField(blank=True, null=True)
    fin = models.DateField(blank=True, null=True)
    estado = models.NullBooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gestion'

class Programa(models.Model):
    nombreprograma = models.CharField(max_length=50, blank=True, null=True)
    idunidad = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='idunidad', blank=True, null=True)
    idgestion = models.ForeignKey(Gestion, models.DO_NOTHING, db_column='idgestion', blank=True, null=True)
    codigosigma = models.IntegerField(blank=True, null=True)
    idprograma = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'programa'


class Lugar(models.Model):
    idlugar = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
    municipio = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lugar'

class Proyectoactividad(models.Model):
    idproyectoactividad = models.AutoField(primary_key=True)
    nombreproyectoactividad = models.CharField(max_length=250, blank=True, null=True)
    descripcion = models.TextField(max_length=250,blank=True, null=True)
    idprograma = models.ForeignKey(Programa, models.DO_NOTHING, db_column='idprograma', blank=True, null=True)
    codsisin = models.CharField(max_length=15, blank=True, null=True)
    codsigma = models.IntegerField(blank=True, null=True)
    idlugar = models.ForeignKey(Lugar, models.DO_NOTHING, db_column='idlugar', blank=True, null=True)
    tipo = models.CharField(max_length=5, blank=True, null=True)
    pvigente = models.FloatField(blank=True, null=True)
    observacion = models.TextField(max_length=250,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyectoactividad'

class Financiamiento(models.Model):
    idfinanciamiento = models.AutoField(primary_key=True)
    idproyectoactividad = models.ForeignKey('Proyectoactividad', models.DO_NOTHING, db_column='idproyectoactividad', blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    financiador = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financiamiento'

class Frentes(models.Model):
    idfrentes = models.AutoField(primary_key=True)
    frente = models.TextField(max_length=250,blank=True, null=True)  # This field type is a guess.
    imgfrente = models.TextField(max_length=250,blank=True, null=True)
    descripcion_condiciones = models.TextField(blank=True, null=True)
    idproyectoactividad = models.ForeignKey('Proyectoactividad', models.DO_NOTHING, db_column='idproyectoactividad', blank=True, null=True)
    numerofrente = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frentes'

class Localizacion(models.Model):
    idlocalizacion = models.AutoField(primary_key=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    idproyectoactividad = models.ForeignKey('Proyectoactividad', models.DO_NOTHING, db_column='idproyectoactividad', blank=True, null=True)
    comunidad = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localizacion'

class Operacion(models.Model):
    idoperacion = models.AutoField(primary_key=True)
    idproyectoactividad = models.ForeignKey('Proyectoactividad', models.DO_NOTHING, db_column='idproyectoactividad', blank=True, null=True)
    ind_programado = models.CharField(max_length=30, blank=True, null=True)
    ind_alcanzado = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operacion'

class Empresa(models.Model):
    idempresa = models.AutoField(primary_key=True)
    empresa = models.CharField(max_length=250, blank=True, null=True)
    nit = models.CharField(max_length=25, blank=True, null=True)
    representante_legal = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'

class Seguimiento(models.Model):
    idseguimiento = models.AutoField(primary_key=True)
    idproyectoactividad = models.ForeignKey(Proyectoactividad, models.DO_NOTHING, db_column='idproyectoactividad', blank=True, null=True)
    idunidad = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='idunidad', blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seguimiento'


class Responsables(models.Model):
    idresponsable = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idusuario', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    idproyectoactividad = models.ForeignKey(Proyectoactividad, models.DO_NOTHING, db_column='idproyectoactividad', blank=True, null=True)
    idcargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='idcargo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responsables'

class DetalleSeguimiento(models.Model):
    iddetalleseguimiento = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=10, blank=True, null=True)
    fecha_actualizacion = models.DateField(blank=True, null=True)
    detalle = models.CharField(max_length=250, blank=True, null=True)
    idresponsable = models.ForeignKey('Responsables', models.DO_NOTHING, db_column='idresponsable', blank=True, null=True)
    idseguimiento = models.ForeignKey('Seguimiento', models.DO_NOTHING, db_column='idseguimiento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_seguimiento'



class Contrato(models.Model):
    idcontrato = models.AutoField(primary_key=True)
    fecha_adjudicacion = models.DateField(blank=True, null=True)
    fecha_firma_contrato = models.DateField(blank=True, null=True)
    monto_contrato = models.FloatField(blank=True, null=True)
    idproyectoactividad = models.ForeignKey('Proyectoactividad', models.DO_NOTHING, db_column='idproyectoactividad', blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    idempresa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contrato'

class Ordendecambio(models.Model):
    idordendecambio = models.AutoField(primary_key=True)
    montoinicial = models.FloatField(blank=True, null=True)
    montofinal = models.FloatField(blank=True, null=True)
    fechainicial = models.DateField(blank=True, null=True)
    fechafin = models.DateField(blank=True, null=True)
    diasiniciales = models.IntegerField(blank=True, null=True)
    diasadicionales = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    idusuario = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(max_length=250,blank=True, null=True)
    idcontrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='idcontrato', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordendecambio'


class Ejecucion(models.Model):
    idejecucion = models.AutoField(primary_key=True)
    idcontrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='idcontrato', blank=True, null=True)
    plazo_ejecucion = models.IntegerField(blank=True, null=True)
    orden_de_proceder = models.DateField(blank=True, null=True)
    entrega_provisional = models.DateField(blank=True, null=True)
    entrega_definitiva = models.DateField(blank=True, null=True)
    observacion = models.TextField(max_length=250,blank=True, null=True)
    fecha_inicio_obra = models.DateField(blank=True, null=True)
    fecha_conclusion_prog = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ejecucion'


class EjecucionFinanciera(models.Model):
    id_detalle_ejecucion_financiera = models.AutoField(primary_key=True)
    periodo = models.DateField(blank=True, null=True)
    certificado = models.CharField(max_length=15, blank=True, null=True)
    avance_ejecutado = models.FloatField(blank=True, null=True)
    idejecucion = models.ForeignKey(Ejecucion, models.DO_NOTHING, db_column='idejecucion', blank=True, null=True)
    observaciones = models.TextField(max_length=250,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ejecucion_financiera'


class EjecucionFisica(models.Model):
    id_detalle_ejecucion_fisica = models.AutoField(primary_key=True)
    programado = models.FloatField(blank=True, null=True)
    avace_actual = models.FloatField(blank=True, null=True)
    ejecucion_fisica = models.FloatField(blank=True, null=True)
    observaciones = models.TextField(max_length=250,blank=True, null=True)
    idejecucion = models.ForeignKey(Ejecucion, models.DO_NOTHING, db_column='idejecucion', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ejecucion_fisica'


class Galeria(models.Model):
    idgaleria = models.IntegerField(primary_key=True)
    foto = models.TextField(max_length=250,blank=True, null=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    id_detalle_ejecucion_fisica = models.ForeignKey(EjecucionFisica, models.DO_NOTHING, db_column='id_detalle_ejecucion_fisica', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'galeria'


#TODO:
class Configuracion(models.Model):
    idconfiguracion = models.SmallIntegerField(primary_key=True)
    logo = models.TextField()

    class Meta:
        managed = False
        db_table = 'configuracion'
