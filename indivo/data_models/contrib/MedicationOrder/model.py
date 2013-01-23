
from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField, CollaboRhythmValueAndUnitField, RecurrenceRuleField, CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class MedicationOrder(Fact):
    name = CollaboRhythmCodedValueField()
    orderType = models.CharField(max_length=255)
    orderedBy = models.CharField(max_length=255)
    dateOrdered = models.DateTimeField()
    dateExpires = models.DateTimeField(null=True)
    indication = models.CharField(max_length=255, null=True)
    amountOrdered = CollaboRhythmValueAndUnitField(null=True)
    refills = models.IntegerField(null=True)
    substitutionPermitted = models.NullBooleanField()
    instructions = models.CharField(max_length=255, null=True)
