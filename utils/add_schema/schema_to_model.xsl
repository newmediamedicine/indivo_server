<?xml version='1.0' encoding='ISO-8859-1'?>
<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform' xmlns:indivodoc="http://indivo.org/vocab/xml/documents#" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xsl:output method = "text" />
  <xsl:template match="xs:schema">
    <xsl:variable name="name" select="xs:element/@name"/>
from indivo.models import Fact
from django.db import models
from indivo.fields import CollaboRhythmCodedValueField, CollaboRhythmValueAndUnitField, CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class <xsl:value-of select="$name"/>(Fact):
<xsl:for-each select="xs:complexType[@name=$name]/xs:sequence/xs:element">
    <xsl:text>    </xsl:text>
    <xsl:value-of select="@name"/> = <xsl:choose>
      <xsl:when test="(@type = 'indivo:CollaboRhythmCodedValue' or @type = 'indivo:CodedValue') and @minOccurs='0'">CollaboRhythmCodedValueField(null=True)</xsl:when>
      <xsl:when test="(@type = 'indivo:CollaboRhythmCodedValue' or @type = 'indivo:CodedValue')">CollaboRhythmCodedValueField()</xsl:when>
      <xsl:when test="(@type = 'indivo:CollaboRhythmValueAndUnit' or @type = 'indivo:ValueAndUnit') and @minOccurs='0'">CollaboRhythmValueAndUnitField(null=True)</xsl:when>
      <xsl:when test="(@type = 'indivo:CollaboRhythmValueAndUnit' or @type = 'indivo:ValueAndUnit')">CollaboRhythmValueAndUnitField()</xsl:when>
      <xsl:when test="(@type = 'xs:dateTime')">models.DateField()</xsl:when>
      <xsl:when test="(@type = 'xs:boolean') and @minOccurs='0'">models.NullBooleanField()</xsl:when>
      <xsl:when test="(@type = 'xs:boolean')">models.BooleanField()</xsl:when>
      <xsl:when test="(@type = 'xs:integer')">models.IntegerField(<xsl:if test="@minOccurs='0'">null=True</xsl:if>)</xsl:when>
      <xsl:otherwise>models.CharField()</xsl:otherwise>
    </xsl:choose><xsl:text>&#10;</xsl:text>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>
