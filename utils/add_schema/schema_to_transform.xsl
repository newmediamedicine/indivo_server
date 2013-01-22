<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xslout="xslout-namespace" version="1.0" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xsl:output method="xml" indent="yes" />
  <xsl:namespace-alias stylesheet-prefix="xslout" result-prefix="xsl"/>

  <xsl:template match="xs:schema">
    <xsl:variable name="name" select="xs:element/@name"/>
    <xslout:stylesheet version="1.0" xmlns:indivodoc="http://indivo.org/vocab/xml/documents#">
      <xslout:template match="/">
        <Models>
          <Model name="{$name}"><xsl:text>&#10;</xsl:text>
            <xsl:for-each select="xs:complexType[@name=$name]/xs:sequence/xs:element">
              <xsl:variable name="childName" select="@name"/>
              <xsl:choose>

                <xsl:when test="(@type = 'indivo:CollaboRhythmCodedValue' or @type = 'indivo:CodedValue') and @minOccurs='0'">
                  <xslout:if test="indivodoc:{$childName}">
                    <Field name="{$childName}_text"><xslout:value-of select='indivodoc:{$childName}/text()' /></Field>
                    <xslout:if test="indivodoc:{$childName}/@type">
                      <Field name="{$childName}_type"><xslout:value-of select='indivodoc:{$childName}/@type'/></Field>
                    </xslout:if>
                    <xslout:if test="indivodoc:{$childName}/@value">
                      <Field name="{$childName}_value"><xslout:value-of select='indivodoc:{$childName}/@value' /></Field>
                    </xslout:if>
                    <xslout:if test="indivodoc:{$childName}/@abbrev">
                      <Field name="{$childName}_abbrev"><xslout:value-of select='indivodoc:{$childName}/@abbrev' /></Field>
                    </xslout:if>
                  </xslout:if>
                </xsl:when>

                <xsl:when test="(@type = 'indivo:CollaboRhythmCodedValue' or @type = 'indivo:CodedValue')">
                  <Field name="{$childName}_text"><xslout:value-of select='indivodoc:{$childName}/text()' /></Field>
                  <xslout:if test="indivodoc:{$childName}/@type">
                    <Field name="{$childName}_type"><xslout:value-of select='indivodoc:{$childName}/@type'/></Field>
                  </xslout:if>
                  <xslout:if test="indivodoc:{$childName}/@value">
                    <Field name="{$childName}_value"><xslout:value-of select='indivodoc:{$childName}/@value' /></Field>
                  </xslout:if>
                  <xslout:if test="indivodoc:{$childName}/@abbrev">
                    <Field name="{$childName}_abbrev"><xslout:value-of select='indivodoc:{$childName}/@abbrev' /></Field>
                  </xslout:if>
                </xsl:when>

                <xsl:when test="(@type = 'indivo:CollaboRhythmValueAndUnit' or @type = 'indivo:ValueAndUnit') and @minOccurs='0'">
                  <xslout:if test="indivodoc:{$childName}">
                    <xslout:if test="indivodoc:{$childName}/value">
                      <Field name="{$childName}_value"><xslout:value-of select='indivodoc:{$childName}/value'/></Field>
                    </xslout:if>
                    <xslout:if test="indivodoc:{$childName}/textValue">
                      <Field name="{$childName}_textValue"><xslout:value-of select='indivodoc:{$childName}/textValue' /></Field>
                    </xslout:if>
                    <xslout:if test="indivodoc:{$childName}/unit">
                      <Field name="{$childName}_unit_text"><xslout:value-of select='indivodoc:{$childName}/unit/text()' /></Field>
                      <xslout:if test="indivodoc:{$childName}/unit/@type">
                        <Field name="{$childName}_unit_type"><xslout:value-of select='indivodoc:{$childName}/unit/@type'/></Field>
                      </xslout:if>
                      <xslout:if test="indivodoc:{$childName}/unit/@value">
                        <Field name="{$childName}_unit_value"><xslout:value-of select='indivodoc:{$childName}/unit/@value' /></Field>
                      </xslout:if>
                      <xslout:if test="indivodoc:{$childName}/unit/@abbrev">
                        <Field name="{$childName}_unit_abbrev"><xslout:value-of select='indivodoc:{$childName}/unit/@abbrev' /></Field>
                      </xslout:if>
                    </xslout:if>
                  </xslout:if>
                </xsl:when>

                <xsl:when test="(@type = 'indivo:CollaboRhythmValueAndUnit' or @type = 'indivo:ValueAndUnit')">
                  <xslout:if test="indivodoc:{$childName}/value">
                    <Field name="{$childName}_value"><xslout:value-of select='indivodoc:{$childName}/value'/></Field>
                  </xslout:if>
                  <xslout:if test="indivodoc:{$childName}/textValue">
                    <Field name="{$childName}_textValue"><xslout:value-of select='indivodoc:{$childName}/textValue' /></Field>
                  </xslout:if>
                  <xslout:if test="indivodoc:{$childName}/unit">
                    <Field name="{$childName}_unit_text"><xslout:value-of select='indivodoc:{$childName}/unit/text()' /></Field>
                    <xslout:if test="indivodoc:{$childName}/unit/@type">
                      <Field name="{$childName}_unit_type"><xslout:value-of select='indivodoc:{$childName}/unit/@type'/></Field>
                    </xslout:if>
                    <xslout:if test="indivodoc:{$childName}/unit/@value">
                      <Field name="{$childName}_unit_value"><xslout:value-of select='indivodoc:{$childName}/unit/@value' /></Field>
                    </xslout:if>
                    <xslout:if test="indivodoc:{$childName}/unit/@abbrev">
                      <Field name="{$childName}_unit_abbrev"><xslout:value-of select='indivodoc:{$childName}/unit/@abbrev' /></Field>
                    </xslout:if>
                  </xslout:if>
                </xsl:when>

                <xsl:when test="@minOccurs='0'">
                  <xslout:if test="indivodoc:{$childName}">
                    <Field name="{$childName}"><xslout:value-of select='indivodoc:{$childName}/text()'/></Field>
                  </xslout:if>
                </xsl:when>
                <xsl:otherwise>
                  <Field name="{$childName}"><xslout:value-of select='indivodoc:{$childName}/text()'/></Field>
                </xsl:otherwise>
              </xsl:choose><xsl:text>&#10;</xsl:text>
            </xsl:for-each>

            </Model>
          </Models>
      </xslout:template>
    </xslout:stylesheet>
  </xsl:template>
</xsl:stylesheet>