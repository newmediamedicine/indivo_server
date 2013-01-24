from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField

class HealthActionResult(Fact):
    name = CollaboRhythmCodedValueField()
    planType = models.CharField(max_length=255, null=True)
    reportedBy = models.CharField(max_length=255, null=True)
    dateReported = models.DateTimeField(null=True)
    actions = models.TextField(null=True)
