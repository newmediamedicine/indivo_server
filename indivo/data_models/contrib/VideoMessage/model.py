
from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField, CollaboRhythmValueAndUnitField, CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class VideoMessage(Fact):
    fileId = models.CharField(max_length=255)
    storageType = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    #from = models.CharField(max_length=255)
    dateRecorded = models.DateField()
    dateSent = models.DateField()
