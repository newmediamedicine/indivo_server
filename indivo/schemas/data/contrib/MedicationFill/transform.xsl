<?xml version="1.0"?>
<xsl:stylesheet xmlns:indivodoc="http://indivo.org/vocab/xml/documents#" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" version="1.0">
  <xsl:template match="indivodoc:MedicationFill">
    <Models>
      <Model name="MedicationFill">
<Field name="name_text"><xsl:value-of select="indivodoc:name/text()"/></Field><xsl:if test="indivodoc:name/@type"><Field name="name_type"><xsl:value-of select="indivodoc:name/@type"/></Field></xsl:if><xsl:if test="indivodoc:name/@value"><Field name="name_value"><xsl:value-of select="indivodoc:name/@value"/></Field></xsl:if><xsl:if test="indivodoc:name/@abbrev"><Field name="name_abbrev"><xsl:value-of select="indivodoc:name/@abbrev"/></Field></xsl:if>
<Field name="filledBy"><xsl:value-of select="indivodoc:filledBy/text()"/></Field>
<Field name="dateFilled"><xsl:value-of select="indivodoc:dateFilled/text()"/></Field>
<xsl:if test="indivodoc:amountFilled/value"><Field name="amountFilled_value"><xsl:value-of select="indivodoc:amountFilled/value"/></Field></xsl:if><xsl:if test="indivodoc:amountFilled/textValue"><Field name="amountFilled_textValue"><xsl:value-of select="indivodoc:amountFilled/textValue"/></Field></xsl:if><xsl:if test="indivodoc:amountFilled/unit"><Field name="amountFilled_unit_text"><xsl:value-of select="indivodoc:amountFilled/unit/text()"/></Field><xsl:if test="indivodoc:amountFilled/unit/@type"><Field name="amountFilled_unit_type"><xsl:value-of select="indivodoc:amountFilled/unit/@type"/></Field></xsl:if><xsl:if test="indivodoc:amountFilled/unit/@value"><Field name="amountFilled_unit_value"><xsl:value-of select="indivodoc:amountFilled/unit/@value"/></Field></xsl:if><xsl:if test="indivodoc:amountFilled/unit/@abbrev"><Field name="amountFilled_unit_abbrev"><xsl:value-of select="indivodoc:amountFilled/unit/@abbrev"/></Field></xsl:if></xsl:if>
<xsl:if test="indivodoc:ndc"><Field name="ndc_text"><xsl:value-of select="indivodoc:ndc/text()"/></Field><xsl:if test="indivodoc:ndc/@type"><Field name="ndc_type"><xsl:value-of select="indivodoc:ndc/@type"/></Field></xsl:if><xsl:if test="indivodoc:ndc/@value"><Field name="ndc_value"><xsl:value-of select="indivodoc:ndc/@value"/></Field></xsl:if><xsl:if test="indivodoc:ndc/@abbrev"><Field name="ndc_abbrev"><xsl:value-of select="indivodoc:ndc/@abbrev"/></Field></xsl:if></xsl:if>
<xsl:if test="indivodoc:fillSequenceNumber"><Field name="fillSequenceNumber"><xsl:value-of select="indivodoc:fillSequenceNumber/text()"/></Field></xsl:if>
<xsl:if test="indivodoc:lotNumber"><Field name="lotNumber"><xsl:value-of select="indivodoc:lotNumber/text()"/></Field></xsl:if>
<xsl:if test="indivodoc:refillsRemaining"><Field name="refillsRemaining"><xsl:value-of select="indivodoc:refillsRemaining/text()"/></Field></xsl:if>
<xsl:if test="indivodoc:instructions"><Field name="instructions"><xsl:value-of select="indivodoc:instructions/text()"/></Field></xsl:if>
</Model>
    </Models>
  </xsl:template>
</xsl:stylesheet>
