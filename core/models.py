from django.db import models

class PDF(models.Model):
    nombre = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)
    objetivos = models.TextField()#Para textos largos como fundamentos, bibliografia, etc
    condicion = models.CharField(max_length=50, blank=True, null=True)
    curso = models.CharField(max_length=50, blank=True, null=True)
    semestre = models.CharField(max_length=50, blank=True, null=True)
    requisitos = models.TextField(blank=True, null=True)
    carga_horaria_semanal = models.CharField(max_length=100, blank=True, null=True)
    carga_horaria_semestral = models.CharField(max_length=100, blank=True, null=True)
    fundamentacion = models.TextField(blank=True, null=True)
    metodologia = models.TextField(blank=True, null=True)
    evaluacion = models.TextField(blank=True, null=True)
    bibliografia = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.archivo
