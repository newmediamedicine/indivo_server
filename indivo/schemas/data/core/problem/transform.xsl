<?xml version="1.0"?>
<xsl:stylesheet xmlns:indivodoc="http://indivo.org/vocab/xml/documents#"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema"
                version="1.0">
  <xsl:template match="indivodoc:Problem">
    <Models>
      <Model name="Problem">
        <xsl:if test="indivodoc:startDate">
          <Field name="startDate">
            <xsl:value-of select="indivodoc:startDate/text()"/>
          </Field>
        </xsl:if>
        <xsl:if test="indivodoc:endDate">
          <Field name="endDate">
            <xsl:value-of select="indivodoc:endDate/text()"/>
          </Field>
        </xsl:if>
        <xsl:if test="indivodoc:name/indivodoc:title">
          <Field name="name_title">
            <xsl:value-of select="indivodoc:name/indivodoc:title"/>
          </Field>
        </xsl:if>
        <xsl:if test="indivodoc:name/indivodoc:system">
          <Field name="name_system">
            <xsl:value-of select="indivodoc:name/indivodoc:system"/>
          </Field>
        </xsl:if>
        <xsl:if test="indivodoc:name/indivodoc:identifier">
          <Field name="name_identifier">
            <xsl:value-of select="indivodoc:name/indivodoc:identifier"/>
          </Field>
        </xsl:if>
        <xsl:if test="indivodoc:notes">
          <Field name="notes">
            <xsl:value-of select="indivodoc:notes/text()"/>
          </Field>
        </xsl:if>
      </Model>
    </Models>
  </xsl:template>
</xsl:stylesheet>
