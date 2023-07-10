from django.db import models
import os
# Create your models here.
# class FeatureProducts(models.Model):
#     image = models.ImageField(upload_to="featureproducts/")
#     name = models.TextField()
#     value = models.FloatField()
#     description = models.TextField()
#     ratirng = models.FloatField()
class FeatureProducts(models.Model):
    image = models.ImageField(upload_to='featureproducts/',null=True)
    name = models.TextField()
    value = models.FloatField()
    description = models.TextField()
class ProProducts(models.Model):
    image = models.ImageField(upload_to='proproducts/',null=True)
    name = models.TextField()
    value = models.FloatField()
    description = models.TextField()