from django.db import models

# Create your models here.


# db랑 연결시켜주는것
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)