
from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField, CollaboRhythmValueAndUnitField, RecurrenceRuleField, CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class MedicationAdministration(Fact):
    name = CollaboRhythmCodedValueField()
    reportedBy = models.CharField(max_length=255)
    dateReported = models.DateTimeField()
    dateAdministered = models.DateTimeField(null=True)
    amountAdministered = CollaboRhythmValueAndUnitField(null=True)
    amountRemaining = CollaboRhythmValueAndUnitField(null=True)
