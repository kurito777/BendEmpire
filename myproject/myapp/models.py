from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    bith_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.last_name}"
class Manga(models.Model):
    idManga = models.CharField(max_length=13, primary_key=True, unique=True, null=False)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="mangas")
    estado = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} {self.estado} {Author}"
    
class tipo_sub(models.Model):
    estado_sub = models.BooleanField()    
class Subcribcion(models.Model):
    tipo_sub = models.ForeignKey(tipo_sub, on_delete=models.CASCADE, related_name="mangas")