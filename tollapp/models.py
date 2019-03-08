from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class TollCmpReg_Model(models.Model):

    tollid = models.CharField(max_length=100)
    tollcmpname= models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class TaxpayerReg_Model(models.Model):

    vehicleno = models.CharField(max_length=100)
    taxpayername= models.CharField(max_length=255)
    vtype = models.CharField(max_length=255)
