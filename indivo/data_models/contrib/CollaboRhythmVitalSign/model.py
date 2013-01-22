
from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField, CollaboRhythmValueAndUnitField, CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class VitalSign(Fact):
