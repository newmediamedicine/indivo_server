<?xml version='1.0' encoding='ISO-8859-1'?>
<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform' xmlns:indivodoc="http://indivo.org/vocab/xml/documents#">
  <xsl:output method = "xml" indent = "yes" />
  <xsl:template match="indivodoc:MedicationOrder">
    <Models>
      <Model name="MedicationOrder">
        <Field name="name_text"><xsl:value-of select='indivodoc:name/text()' /></Field>
        <xsl:if test="indivodoc:name/@type">
          <Field name="name_type"><xsl:value-of select='indivodoc:name/@type'/></Field>
        </xsl:if>
        <xsl:if test="indivodoc:name/@value">
          <Field name="name_value"><xsl:value-of select='indivodoc:name/@value' /></Field>
        </xsl:if>
        <xsl:if test="indivodoc:name/@abbrev">
          <Field name="name_abbrev"><xsl:value-of select='indivodoc:name/@abbrev' /></Field>
        </xsl:if>
        <Field name="orderType"><xsl:value-of select='indivodoc:orderType/text()'/></Field>
        <Field name="orderedBy"><xsl:value-of select='indivodoc:orderedBy/text()'/></Field>
        <Field name="dateOrdered"><xsl:value-of select='indivodoc:dateOrdered/text()' /></Field>
        <xsl:if test="indivodoc:dateExpires">
          <Field name="dateExpires"><xsl:value-of select='indivodoc:dateExpires/text()'/></Field>
        </xsl:if>
        <xsl:if test="indivodoc:indication">
          <Field name="indication"><xsl:value-of select='indivodoc:indication/text()'/></Field>
        </xsl:if>
        <xsl:if test="indivodoc:amountOrdered">
          <xsl:if test="indivodoc:amountOrdered/value">
            <Field name="amountOrdered_value"><xsl:value-of select="indivodoc:amountOrdered/value/text()"/></Field>
          </xsl:if>
          <xsl:if test="indivodoc:amountOrdered/textValue">
            <Field name="amountOrdered_textValue"><xsl:value-of select="indivodoc:amountOrdered/textValue/text()"/></Field>
          </xsl:if>
          <xsl:if test="indivodoc:amountOrdered/unit">
            <Field name="amountOrdered_unit_text"><xsl:value-of select='indivodoc:amountOrdered/unit/text()' /></Field>
            <xsl:if test="indivodoc:amountOrdered/unit/@type">
              <Field name="amountOrdered_unit_type"><xsl:value-of select='indivodoc:amountOrdered/unit/@type'/></Field>
            </xsl:if>
            <xsl:if test="indivodoc:amountOrdered/unit/@value">
              <Field name="amountOrdered_unit_value"><xsl:value-of select='indivodoc:amountOrdered/unit/@value' /></Field>
            </xsl:if>
            <xsl:if test="indivodoc:amountOrdered/unit/@abbrev">
              <Field name="amountOrdered_unit_abbrev"><xsl:value-of select='indivodoc:amountOrdered/unit/@abbrev' /></Field>
            </xsl:if>
          </xsl:if>
        </xsl:if>
        <xsl:if test="indivodoc:refills">
          <Field name="refills"><xsl:value-of select='indivodoc:refills/text()'/></Field>
        </xsl:if>
        <xsl:if test="indivodoc:substitutionPermitted">
          <Field name="substitutionPermitted"><xsl:value-of select='indivodoc:substitutionPermitted/text()'/></Field>
        </xsl:if>
        <xsl:if test="indivodoc:instructions">
          <Field name="instructions"><xsl:value-of select='indivodoc:instructions/text()'/></Field>
        </xsl:if>
      </Model>
    </Models>
  </xsl:template>
</xsl:stylesheet>