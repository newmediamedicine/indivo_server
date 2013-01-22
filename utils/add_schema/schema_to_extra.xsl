<?xml version='1.0' encoding='ISO-8859-1'?>
<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform' xmlns:indivodoc="http://indivo.org/vocab/xml/documents#" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xsl:output method = "text" />
  <xsl:template match="xs:schema">
    <xsl:variable name="name" select="xs:element/@name"/>
from indivo.serializers import DataModelSerializers
from indivo.data_models.options import DataModelOptions
from indivo.lib.rdf import PatientGraph
from indivo.validators import ValueInSetValidator, ExactValueValidator, NonNullValidator
from indivo.lib import utils

class <xsl:value-of select="$name"/>Serializers(DataModelSerializers):

    def to_xml(query, record=None, carenet=None):
        if not record:
            record = carenet.record

        return query.render("reports/contrib/<xsl:value-of select="$name"/>.xml")

class <xsl:value-of select="$name"/>Options(DataModelOptions):
    model_class_name = '<xsl:value-of select="$name"/>'
    serializers = <xsl:value-of select="$name"/>Serializers
  </xsl:template>
</xsl:stylesheet>
