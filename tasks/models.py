from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['status']),
        ]

