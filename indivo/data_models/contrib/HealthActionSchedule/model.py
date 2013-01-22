
from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField, CollaboRhythmValueAndUnitField, CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class HealthActionSchedule(Fact):
    name = CollaboRhythmCodedValueField()
    scheduledBy = models.CharField(max_length=255)
    dateScheduled = models.DateField()
    dateStart = models.DateField()
    dateEnd = models.DateField(null=True)
    recurrenceRule = models.CharField(max_length=255, null=True)
    instructions = models.CharField(max_length=255, null=True)
