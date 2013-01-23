from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField

class HealthActionPlan(Fact):
    name = CollaboRhythmCodedValueField()
    planType = models.CharField(max_length=255)
    plannedBy = models.CharField(max_length=255)
    datePlanned = models.DateField()
    dateExpires = models.DateField(null=True)
    indication = models.CharField(max_length=255)
    instructions = models.CharField(max_length=255)
    system = CollaboRhythmCodedValueField()
    actions = models.TextField(null=True)