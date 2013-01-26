from indivo.models import Fact
from django.db import models

class Wellness(Fact):
    measurementDate = models.DateTimeField(null=True)
    reportedBy = models.CharField(max_length=255)
    dateReported = models.DateTimeField()
    numberOfStepsTaken = models.IntegerField()
    numberOfHoursSlept = models.FloatField()
    numberOfTimesAwakened = models.IntegerField()
