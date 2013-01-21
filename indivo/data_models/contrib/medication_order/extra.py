from indivo.serializers import DataModelSerializers
from indivo.data_models.options import DataModelOptions
from indivo.lib.rdf import PatientGraph
from indivo.validators import ValueInSetValidator, ExactValueValidator, NonNullValidator
from indivo.lib import utils

class MedicationOrderSerializers(DataModelSerializers):

    def to_xml(query, record=None, carenet=None):
        if not record:
            record = carenet.record

        return query.render("reports/medicationorder") #utils.render_template_raw("medicationorder", {'fobj': queryset})
#        return utils.render_template_raw("reports/medicationorder", {'fobj': query.results[0]})

class MedicationOrderOptions(DataModelOptions):
    model_class_name = 'MedicationOrder'
    serializers = MedicationOrderSerializers
