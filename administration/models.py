from django.db import models

# Create your models here.
class Provider(models.Model):
    first_name = models.CharField(max_length=128, verbose_name="Nombres")
    last_name = models.CharField(max_length=128, verbose_name="Apellidos")
    main_photo = models.ImageField(upload_to="providers/", 
                                   blank=True, null=True, 
                                   verbose_name="Selecciona la foto")
    description = models.TextField(verbose_name="Describe al paseador")
    
    class Meta:
        verbose_name_plural = "Paseadores"
        verbose_name = "Paseador"

class Customer(models.Model):
    first_name = models.CharField(max_length=128, verbose_name="Nombres")
    last_name = models.CharField(max_length=128, verbose_name="Apellidos")
    address = models.CharField(max_length=128, verbose_name="Direccion")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"

class Pet(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT) # Llave foranea
    name = models.CharField(max_length=128)
    age = models.CharField(max_length=64)
    pedigree = models.CharField(max_length=128)
    main_photo = models.ImageField(upload_to="pets/", 
                                   blank=True, null=True, )
    class Meta:
        verbose_name_plural = "Mascotas"
        verbose_name = "Mascota"
