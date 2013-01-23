
from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField, CollaboRhythmValueAndUnitField, RecurrenceRuleField, CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class MedicationScheduleItem(Fact):
    name = CollaboRhythmCodedValueField()
    scheduledBy = models.CharField(max_length=255)
    dateScheduled = models.DateField()
    dateStart = models.DateField()
    dateEnd = models.DateField(null=True)
    recurrenceRule = RecurrenceRuleField(null=True)
    dose = CollaboRhythmValueAndUnitField()
    instructions = models.CharField(max_length=255, null=True)
