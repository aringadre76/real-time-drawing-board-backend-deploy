from django.db import models

class Drawing(models.Model):
    user = models.CharField(max_length=100)  # Example user identifier
    data = models.TextField()  # Could store drawing data as JSON
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Drawing by {self.user} at {self.created_at}"
