from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField, CollaboRhythmValueAndUnitField, CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class MedicationOrder(Fact):
#    name_text = models.CharField(max_length=255)
    name = CollaboRhythmCodedValueField()
#    name_type = models.CharField(max_length=255)
#    name_value = models.CharField(max_length=255)
#    name_abbrev = models.CharField(max_length=255)
    orderType = models.CharField(max_length=255)
    orderedBy = models.CharField(max_length=255)
    dateOrdered = models.DateField()
    dateExpires = models.DateField()
    indication = models.CharField(max_length=255, null=True)
    amountOrdered = CollaboRhythmValueAndUnitField(null=True)
    refills = models.IntegerField(null=True)
    substitutionPermitted = models.NullBooleanField()
    instructions = models.CharField(max_length=255, null=True)
