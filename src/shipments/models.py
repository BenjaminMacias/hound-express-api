from django.db import models

class Guide(models.Model):
    number = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING',    'Pendiente'),
            ('IN_TRANSIT', 'En tránsito'),
            ('DELIVERED',  'Entregado'),
        ],
        default='PENDING'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number

class StatusChange(models.Model):
    guide = models.ForeignKey(Guide, related_name='history', on_delete=models.CASCADE)
    previous = models.CharField(max_length=20)
    new = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guide.number}: {self.previous} → {self.new}"
