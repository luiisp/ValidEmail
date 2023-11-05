from django.db import models

class Mail(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=5)
