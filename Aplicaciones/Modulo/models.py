from django.db import models

class Carrera(models.Model):
    id_carrera = models.IntegerField(primary_key=True)
    nom_carrera = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_carrera

class Cuatrimestre(models.Model):
    id_cuatrimestre = models.IntegerField(primary_key=True)
    nombre_cuatrimestre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_cuatrimestre

class Libro(models.Model):
    codigo_interno = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    disponibles = models.IntegerField()
    estado_libro = models.CharField(max_length=50)
    idioma = models.CharField(max_length=30)
    editorial = models.CharField(max_length=50)
    paginas = models.IntegerField()
    imagen = models.ImageField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        texto = '({0}) - {1}'
        return texto.format(self.codigo_interno, self.titulo,)

class Alumno(models.Model):
    matricula = models.IntegerField(primary_key=True)
    turno = models.CharField(max_length=50)
    nombre_completo = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    id_cuatrimestre = models.ForeignKey(Cuatrimestre, on_delete=models.CASCADE)

    def __str__(self):
        texto = '({0}) - {1}'
        return texto.format(self.matricula, self.nombre_completo,)

class Prestamo(models.Model):
    id_prestamo = models.IntegerField(primary_key=True)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    matricula = models.ForeignKey(Alumno, on_delete=models.CASCADE)

class Det_Prestamo(models.Model):
    cns = models.IntegerField(primary_key=True)
    cant_libros = models.IntegerField()
    estatus = models.CharField(max_length=50)
    id_prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)

class Historial_Sancions(models.Model):
    const = models.IntegerField(primary_key=True)
    sancion = models.CharField(max_length=100)
    fecha_sancion = models.DateField()
    fecha_vencimiento_sancion = models.DateField()
    cns = models.ForeignKey(Det_Prestamo, on_delete=models.CASCADE)

