from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Alumno(models.Model):
    usuario = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    alumno =models.CharField(max_length=200)
    observacion =models.TextField(null=True,
                                  blank=True)
    completo =models.BooleanField(default=False)
    fecha =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alumno

    class Meta:
        ordering = ["completo"]