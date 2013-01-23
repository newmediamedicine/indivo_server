from indivo.serializers import DataModelSerializers
from indivo.data_models.options import DataModelOptions

class HealthActionPlanSerializers(DataModelSerializers):

    def to_xml(query, record=None, carenet=None):
        if not record:
            record = carenet.record

        return query.render("reports/contrib/HealthActionPlan.xml")

class HealthActionPlanOptions(DataModelOptions):
    model_class_name = 'HealthActionPlan'
    serializers = HealthActionPlanSerializers
    