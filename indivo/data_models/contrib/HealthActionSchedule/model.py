
from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField, CollaboRhythmValueAndUnitField, RecurrenceRuleField, CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class HealthActionSchedule(Fact):
    name = CollaboRhythmCodedValueField()
    scheduledBy = models.CharField(max_length=255)
    dateScheduled = models.DateTimeField()
    dateStart = models.DateTimeField()
    dateEnd = models.DateTimeField(null=True)
    recurrenceRule = RecurrenceRuleField(null=True)
    instructions = models.CharField(max_length=255, null=True)
