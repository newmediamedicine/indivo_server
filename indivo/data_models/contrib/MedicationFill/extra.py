from indivo.serializers import DataModelSerializers
from indivo.data_models.options import DataModelOptions
from indivo.lib.rdf import PatientGraph
from indivo.validators import ValueInSetValidator, ExactValueValidator, NonNullValidator
from indivo.lib import utils

class MedicationFillSerializers(DataModelSerializers):

    def to_xml(query, record=None, carenet=None):
        if not record:
            record = carenet.record

        return query.render("reports/contrib/MedicationFill.xml")

class MedicationFillOptions(DataModelOptions):
    model_class_name = 'MedicationFill'
    serializers = MedicationFillSerializers
  