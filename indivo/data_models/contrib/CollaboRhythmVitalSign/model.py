
from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField, CollaboRhythmValueAndUnitField, RecurrenceRuleField, CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class CollaboRhythmVitalSign(Fact):
    name = CollaboRhythmCodedValueField()
    measuredBy = models.CharField(max_length=255, null=True)
    dateMeasuredStart = models.DateTimeField()
    dateMeasuredEnd = models.DateTimeField(null=True)
    result = CollaboRhythmValueAndUnitField()
    site = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=255, null=True)
    technique = models.CharField(max_length=255, null=True)
    comments = models.CharField(max_length=255, null=True)
