from django.db import models
from django.utils import timezone

class Guia(models.Model):
    id = models.AutoField(primary_key=True)
    trackingNumber = models.CharField(max_length=15)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now=True)
    currentStatus = models.CharField(max_length=20)
    recipient = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.trackingNumber

class Estatus(models.Model):
    id = models.AutoField(primary_key=True)
    guia = models.ForeignKey(
        Guia,
        on_delete=models.CASCADE,
        related_name="estatuses",
        db_column="guideId",
    )
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(default=timezone.now)
    updatedBy = models.CharField(max_length=20)

    class Meta:
        db_table = 'StatusHistory'
        verbose_name = 'Estatus'
        verbose_name_plural = 'Estatus'

    def __str__(self):
        return f"{self.guia.trackingNumber} – {self.status}"

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
