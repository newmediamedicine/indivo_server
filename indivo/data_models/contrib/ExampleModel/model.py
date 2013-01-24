from indivo.models import Fact
from indivo.fields import CollaboRhythmCodedValueField
from django.db import models

class ExampleModel(Fact):
    name = CollaboRhythmCodedValueField()
    startDate = models.DateTimeField(null=True)
    notes = models.TextField(null=True)
