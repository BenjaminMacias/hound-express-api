from django.contrib import admin
from .models import Guia, Estatus, Usuario

@admin.register(Guia)
class GuiaAdmin(admin.ModelAdmin):
    list_display = ('trackingNumber', 'currentStatus', 'createdAt')

@admin.register(Estatus)
class EstatusAdmin(admin.ModelAdmin):
    list_display = ('guia', 'status', 'timestamp', 'updatedBy')
    list_filter = ('status',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'createdAt')
