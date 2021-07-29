from django.db import models

# Create your models here.
class Art(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to ="uploads/art/")