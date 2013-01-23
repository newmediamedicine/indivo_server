<?xml version="1.0"?>
<xsl:stylesheet xmlns:indivodoc="http://indivo.org/vocab/xml/documents#" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" version="1.0">
  <xsl:template match="indivodoc:HealthActionResult">
    <Models>
      <Model name="HealthActionResult">
<Field name="name_text"><xsl:value-of select="indivodoc:name/text()"/></Field><xsl:if test="indivodoc:name/@type"><Field name="name_type"><xsl:value-of select="indivodoc:name/@type"/></Field></xsl:if><xsl:if test="indivodoc:name/@value"><Field name="name_value"><xsl:value-of select="indivodoc:name/@value"/></Field></xsl:if><xsl:if test="indivodoc:name/@abbrev"><Field name="name_abbrev"><xsl:value-of select="indivodoc:name/@abbrev"/></Field></xsl:if>
<xsl:if test="indivodoc:planType"><Field name="planType"><xsl:value-of select="indivodoc:planType/text()"/></Field></xsl:if>
<xsl:if test="indivodoc:reportedBy"><Field name="reportedBy"><xsl:value-of select="indivodoc:reportedBy/text()"/></Field></xsl:if>
<xsl:if test="indivodoc:dateReported"><Field name="dateReported"><xsl:value-of select="indivodoc:dateReported/text()"/></Field></xsl:if>
<xsl:if test="indivodoc:actions"><Field name="actions"><xsl:value-of select="indivodoc:actions/text()"/></Field></xsl:if>
</Model>
    </Models>
  </xsl:template>
</xsl:stylesheet>
