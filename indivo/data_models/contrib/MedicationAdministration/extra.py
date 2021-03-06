
from indivo.serializers import DataModelSerializers
from indivo.data_models.options import DataModelOptions
from indivo.lib.rdf import PatientGraph
from indivo.validators import ValueInSetValidator, ExactValueValidator, NonNullValidator
from indivo.lib import utils

class MedicationAdministrationSerializers(DataModelSerializers):

    def to_xml(query, record=None, carenet=None):
        if not record:
            record = carenet.record

        return query.render("reports/contrib/MedicationAdministration.xml")

class MedicationAdministrationOptions(DataModelOptions):
    model_class_name = 'MedicationAdministration'
    serializers = MedicationAdministrationSerializers
  