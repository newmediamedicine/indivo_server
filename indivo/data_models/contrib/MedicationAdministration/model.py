
from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField, CollaboRhythmValueAndUnitField, CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class MedicationAdministration(Fact):
    name = CollaboRhythmCodedValueField()
    reportedBy = models.CharField(max_length=255)
    dateReported = models.DateField()
    dateAdministered = models.DateField(null=True)
    amountAdministered = CollaboRhythmValueAndUnitField(null=True)
    amountRemaining = CollaboRhythmValueAndUnitField(null=True)