from django.db import models

# Create your models here.
class settingsLog(models.Model):
    input = models.CharField(max_length=300)
    output = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
