from django.db import models

class FurniturePrediction(models.Model):
    image = models.ImageField(upload_to='uploads/')
    prediction = models.CharField(max_length=255)
