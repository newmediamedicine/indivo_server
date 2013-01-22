<?xml version="1.0"?>
<xsl:stylesheet xmlns:indivodoc="http://indivo.org/vocab/xml/documents#" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" version="1.0">
  <xsl:template match="indivodoc:VideoMessage">
    <Models>
      <Model name="VideoMessage">
<Field name="fileId"><xsl:value-of select="indivodoc:fileId/text()"/></Field>
<Field name="storageType"><xsl:value-of select="indivodoc:storageType/text()"/></Field>
<Field name="subject"><xsl:value-of select="indivodoc:subject/text()"/></Field>
<Field name="from"><xsl:value-of select="indivodoc:from/text()"/></Field>
<Field name="dateRecorded"><xsl:value-of select="indivodoc:dateRecorded/text()"/></Field>
<Field name="dateSent"><xsl:value-of select="indivodoc:dateSent/text()"/></Field>
</Model>
    </Models>
  </xsl:template>
</xsl:stylesheet>
