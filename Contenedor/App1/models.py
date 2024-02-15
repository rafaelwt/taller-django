from django.db import models

# Create your models here.


class ProfesionDb(models.Model):
    '''This is the model for the professions of the authors'''
    nombre = models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        '''This is the metadata for the model'''
        db_table = 'Profesiones'
        verbose_name = 'Profesión'
        verbose_name_plural = 'Profesiones'

    def __str__(self) -> str:
        """__str__ returns a string representation of the object."""
        return str(self.nombre)


class AutorDb(models.Model):
    '''This is the model for the authors of the books'''
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    fecha_nacimiento = models.DateField(
        verbose_name='Fecha de nacimiento', null=False, blank=False)
    fecha_fallecimiento = models.DateField(
        'Fecha de fallecimiento', null=True, blank=True)
    # profesion = models.CharField(max_length=50, verbose_name='Profesión')
    profesion = models.ManyToManyField(ProfesionDb, verbose_name='Profesión')
    nacionalidad = models.CharField(max_length=50, verbose_name='Nacionalidad')

    class Meta:
        '''This is the metadata for the model'''
        db_table = 'Autores'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self) -> str:
        """__str__ returns a string representation of the object."""
        return str(self.nombre)


class FraseDb(models.Model):
    '''This is the model for the phrases of the authors'''
    cita = models.TextField(verbose_name='Cita', max_length=500)
    autor_fk = models.ForeignKey(AutorDb, on_delete=models.CASCADE)

    class Meta:
        '''This is the metadata for the model'''
        db_table = 'Frases'
        verbose_name = 'Frase'
        verbose_name_plural = 'Frases'
