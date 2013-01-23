
from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField, CollaboRhythmValueAndUnitField, RecurrenceRuleField, CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class MedicationFill(Fact):
    name = CollaboRhythmCodedValueField()
    filledBy = models.CharField(max_length=255, null=True)
    dateFilled = models.DateTimeField(null=True)
    amountFilled = CollaboRhythmValueAndUnitField(null=True)
    ndc = CollaboRhythmCodedValueField(null=True)
    fillSequenceNumber = models.IntegerField(null=True)
    lotNumber = models.IntegerField(null=True)
    refillsRemaining = models.IntegerField(null=True)
    instructions = models.CharField(max_length=255, null=True)
