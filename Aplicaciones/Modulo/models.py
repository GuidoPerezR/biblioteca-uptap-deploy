from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class Carrera(models.Model):
    id_carrera = models.BigAutoField(primary_key=True)
    nom_carrera = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nom_carrera)

class Libro(models.Model):
    codigo_interno = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    disponibles = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    estado_libro = models.CharField(max_length=50)
    idioma = models.CharField(max_length=30)
    editorial = models.CharField(max_length=50)
    paginas = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3000)])
    imagen = models.ImageField(upload_to='media/booksImages/')
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo} - {self.codigo_interno}'

class Cargo (models.Model):
    id_cargo= models.BigAutoField(primary_key=True)
    nombre= models.CharField(max_length=20)
    def __str__(self):
        return str(self.nombre)

class Usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    turno = models.CharField(max_length=50)
    nombre_completo = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    id_cargo= models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_completo} - {self.id_cargo.nombre}'

class Prestamo(models.Model):
    id_prestamo = models.BigAutoField(primary_key=True)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField()
    matricula = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.matricula.nombre_completo} - {self.id_prestamo}'

class Det_Prestamo(models.Model):
    id_det_prestamo = models.BigAutoField(primary_key=True)
    cant_libros = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])
    estatus = models.CharField(max_length=50)
    id_prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_prestamo.matricula.nombre_completo} - {self.id_prestamo.id_prestamo}'

""" class Historial_Sancions(models.Model):
    const = models.IntegerField(primary_key=True)
    sancion = models.CharField(max_length=100)
    fecha_sancion = models.DateField()
    fecha_vencimiento_sancion = models.DateField()
    cns = models.ForeignKey(Det_Prestamo, on_delete=models.CASCADE) """


