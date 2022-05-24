from django.db import models

# Create your models here.
class  Proveedor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    cedula=models.CharField(max_length=50)
    celular=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    producto=models.CharField(max_length=50)
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name="Proveedor"
        verbose_name_plural="Proveedores"

    def __str__(self):
        return '{}-{}'.format(self.nombre, self.producto)
