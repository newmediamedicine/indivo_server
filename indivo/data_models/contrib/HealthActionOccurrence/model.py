
from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField, CollaboRhythmValueAndUnitField, CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class HealthActionOccurrence(Fact):
    name = CollaboRhythmCodedValueField()
    recurrenceIndex = models.IntegerField(null=True)
