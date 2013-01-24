from indivo.serializers import DataModelSerializers
from indivo.data_models.options import DataModelOptions

class ExampleModelSerializers(DataModelSerializers):

    def to_xml(query, record=None, carenet=None):
        if not record:
            record = carenet.record

        return query.render("reports/contrib/ExampleModel.xml")

class ExampleModelOptions(DataModelOptions):
    model_class_name = 'ExampleModel'
    serializers = ExampleModelSerializers
  
