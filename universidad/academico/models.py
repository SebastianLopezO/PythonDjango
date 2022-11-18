from django.db import models


# Create your models here.

# FACULTADES
class Facultad(models.Model) :
    id = models.BigAutoField(verbose_name="CÓDIGO", primary_key=True)
    name = models.CharField(verbose_name="FACULTAD", max_length=40)
    description = models.CharField(verbose_name="RESUMEN", max_length=200)
    decano = models.CharField(verbose_name="DECANO", max_length=40)
    secretary = models.CharField(verbose_name="SECRETARIA", max_length=40)

# CARRERAS
class Carrera(models.Model) :
    id = models.BigAutoField(verbose_name="CÓDIGO", primary_key=True)
    name = models.CharField(verbose_name="CARRERA", max_length=40)
    description = models.CharField(verbose_name="RESUMEN", max_length=200)
    creditos = models.PositiveSmallIntegerField(verbose_name="CRÉDITOS")
    faculty = models.ForeignKey(Facultad, on_delete=models.CASCADE, verbose_name="FACULTAD")

# DOCENTES
class Docente(models.Model) :
    id = models.BigAutoField(verbose_name="CÓDIGO", primary_key=True)
    name = models.CharField(verbose_name="NOMBRE", max_length=20)
    lastname = models.CharField(verbose_name="APELLIDO", max_length=20)
    document = models.PositiveIntegerField(verbose_name="CÉDULA", unique=True)
    mail = models.EmailField(verbose_name="CORREO")

# CURSOS, begin, end, creditos, teacher, horario, carrera
class Curso(models.Model) :
    id = models.BigAutoField(verbose_name="CÓDIGO", primary_key=True)
    name = models.CharField(verbose_name="CURSO", max_length=30)
    description = models.CharField(verbose_name="CURSO", max_length=30, blank=True, null=True)
    begin = models.DateField(verbose_name="Fecha inicio")
    end = models.DateField(verbose_name="Fecha terminación")
    creditos = models.PositiveSmallIntegerField(verbose_name="CRÉDITOS")
    teacher = models.ForeignKey(Docente, blank=True, null=True, on_delete=models.SET_NULL)
    horarios = [("D", "DIURNO"), ("N", "NOCTURNO"), ("FDS", "FIN DE SEMANA")]
    horario = models.CharField(verbose_name="JORNADA", max_length=3, choices=horarios)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    # CRUD
    # CREATE
    # READ
    # UPDATE
    # DELETE

    # CREAR NUEVOS REGISTROS (ESTÁNDAR)
    # UPDATE - CREAR
    # VISUALIZAR LA INFORMACIÓN - LISTA O TABLA
    # ACTUALIZAR Y ELIMINAR
    # comandos de shell
