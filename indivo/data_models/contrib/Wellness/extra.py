from indivo.serializers import DataModelSerializers
from indivo.data_models.options import DataModelOptions

class WellnessSerializers(DataModelSerializers):

    def to_xml(query, record=None, carenet=None):
        if not record:
            record = carenet.record

        return query.render("reports/contrib/Wellness.xml")

class WellnessOptions(DataModelOptions):
    model_class_name = 'Wellness'
    serializers = WellnessSerializers
  
