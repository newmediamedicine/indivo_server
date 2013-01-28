from indivo.serializers import DataModelSerializers
from indivo.data_models.options import DataModelOptions
from indivo.lib.rdf import PatientGraph
from indivo.validators import ValueInSetValidator, ExactValueValidator, NonNullValidator

SNOMED_URI = 'http://purl.bioontology.org/ontology/SNOMEDCT/'

class ProblemSerializers(DataModelSerializers):

    def to_rdf(queryset, result_count, record=None, carenet=None):
        if not record:
            record = carenet.record
        
        graph = PatientGraph(record)
        graph.addProblemList(queryset.iterator())
        return graph.toRDF()

    def to_xml(query, record=None, carenet=None):
        if not record:
            record = carenet.record

        return query.render("reports/problem.xml")

class ProblemOptions(DataModelOptions):
    model_class_name = 'Problem'
    serializers = ProblemSerializers
    field_validators = {
        'name_system': [ExactValueValidator(SNOMED_URI)],
        'name_identifier': [NonNullValidator()],
        'name_title': [NonNullValidator()],
        'startDate': [NonNullValidator()],
        }
