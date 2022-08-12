from django.db import models

class ProductData(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=20)
    pcost=models.IntegerField()
    pcolor=models.CharField(max_length=20)
    quantity=models.IntegerField()
    pclass=models.CharField(max_length=20)
    pmdate=models.DateTimeField()
    pedate=models.DateTimeField()