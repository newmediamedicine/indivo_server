
from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField, CollaboRhythmValueAndUnitField, RecurrenceRuleField, CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class AdherenceItem(Fact):
    name = CollaboRhythmCodedValueField()
    reportedBy = models.CharField(max_length=255)
    dateReported = models.DateTimeField()
    recurrenceIndex = models.IntegerField(null=True)
    adherence = models.BooleanField()
    nonadherenceReason = models.CharField(max_length=255, null=True)
