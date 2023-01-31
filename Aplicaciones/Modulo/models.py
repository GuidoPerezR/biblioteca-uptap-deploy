from django.db import models

class Libro(models.Model):
    codigo_interno = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    existencia = models.IntegerField()
    fecha_publicacion = models.DateField()
    estado_libro = models.CharField(max_length=50)

class Carrera(models.Model):
    id_carrera = models.IntegerField(primary_key=True)
    nom_carrera = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_carrera

class Cargo(models.Model):
    id_cargo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Cuatrimestre(models.Model):
    id_cuatrimestre = models.IntegerField(primary_key=True)
    nombre_cuatrimestre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_cuatrimestre

class Alumno(models.Model):
    matricula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    turno = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    id_cuatrimestre = models.ForeignKey(Cuatrimestre, on_delete=models.CASCADE)

    def __str__(self):
        texto = '({0}) - {1} {2}'
        return texto.format(self.matricula, self.nombre, self.apellidos)

class Docente_administrativo(models.Model):
    id_doc_ad = models.IntegerField(primary_key=True)
    turno = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    id_cuatrimestre = models.ForeignKey(Cuatrimestre, on_delete=models.CASCADE)

class Administrador(models.Model):
    id_admin = models.IntegerField(primary_key=True)
    turno = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    id_admin = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    id_doc_ad = models.ForeignKey(Docente_administrativo, on_delete=models.CASCADE)
    matricula = models.ForeignKey(Alumno, on_delete=models.CASCADE)    
