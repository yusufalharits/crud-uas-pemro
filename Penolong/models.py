from sqlite3 import Date
from django.db import models

# Create your models here.

class Jenis(models.Model):
    jenis = models.CharField(max_length=20)

    def __str__(self):
        return self.jenis

class Hewan(models.Model):
    Nama        = models.CharField(max_length=90)
    Deskripsi   = models.TextField(null=True)
    Pemilik     = models.CharField(max_length=90)
    Nomor       = models.IntegerField()
    Date        = models.DateTimeField()
    Jenis_id    = models.ForeignKey(Jenis,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Nama

