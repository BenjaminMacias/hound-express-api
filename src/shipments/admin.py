from django.contrib import admin
from .models import Guide, StatusChange

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ("number", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("number",)

@admin.register(StatusChange)
class StatusChangeAdmin(admin.ModelAdmin):
    list_display = ("guide", "previous", "new", "timestamp")
    list_filter = ("previous", "new")
    search_fields = ("guide__number",)
