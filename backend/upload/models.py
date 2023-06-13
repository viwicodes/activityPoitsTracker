from django.db import models

# Create your models here.
class Cerficate(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=100)
    file = models.ImageField(upload_to="certificates", blank=True)

    def __str__(self):
        return f"{self.owner} - {self.file}"
