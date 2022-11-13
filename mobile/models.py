from django.db import models


class Information(models.Model):
    titre = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    date_de_creation = models.DateTimeField(auto_now=True)
    source = models.CharField(max_length=50)
    image = models.ImageField(upload_to="informations/", null=True, blank=True)
