<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xslout="xslout-namespace" version="1.0" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xsl:output method="xml" indent="yes" />
  <xsl:namespace-alias stylesheet-prefix="xslout" result-prefix="xsl"/>

  <xsl:template match="xs:schema">
    <xsl:variable name="name" select="xs:element/@name"/>
    <xslout:stylesheet version="1.0" xmlns:indivodoc="http://indivo.org/vocab/xml/documents#">
      <xslout:template match="indivodoc:{$name}">
        <Models>
          <Model name="{$name}"><xsl:text>&#10;</xsl:text>
            <xsl:for-each select="xs:complexType[@name=$name]/xs:sequence/xs:element">
              <xsl:variable name="childName" select="@name"/>
              <xsl:choose>

                <xsl:when test="(@type = 'indivo:CodedValue')">
                  <xslout:if test="indivodoc:{$childName}/indivodoc:identifier">
                    <Field name="{$childName}_identifier"><xslout:value-of select='indivodoc:{$childName}/indivodoc:identifier'/></Field>
                  </xslout:if>
                  <xslout:if test="indivodoc:{$childName}/indivodoc:title">
                    <Field name="{$childName}_title"><xslout:value-of select='indivodoc:{$childName}/indivodoc:title' /></Field>
                  </xslout:if>
                  <xslout:if test="indivodoc:{$childName}/indivodoc:system">
                    <Field name="{$childName}_system"><xslout:value-of select='indivodoc:{$childName}/indivodoc:system' /></Field>
                  </xslout:if>
                </xsl:when>

                <xsl:when test="(@type = 'indivo:CollaboRhythmCodedValue') and @minOccurs='0'">
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

                <xsl:when test="(@type = 'indivo:CollaboRhythmCodedValue')">
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
                    <xslout:if test="indivodoc:{$childName}/indivodoc:value">
                      <Field name="{$childName}_value"><xslout:value-of select='indivodoc:{$childName}/indivodoc:value'/></Field>
                    </xslout:if>
                    <xslout:if test="indivodoc:{$childName}/indivodoc:textValue">
                      <Field name="{$childName}_textValue"><xslout:value-of select='indivodoc:{$childName}/indivodoc:textValue' /></Field>
                    </xslout:if>
                    <xslout:if test="indivodoc:{$childName}/indivodoc:unit">
                      <Field name="{$childName}_unit_text"><xslout:value-of select='indivodoc:{$childName}/indivodoc:unit/text()' /></Field>
                      <xslout:if test="indivodoc:{$childName}/indivodoc:unit/@type">
                        <Field name="{$childName}_unit_type"><xslout:value-of select='indivodoc:{$childName}/indivodoc:unit/@type'/></Field>
                      </xslout:if>
                      <xslout:if test="indivodoc:{$childName}/indivodoc:unit/@value">
                        <Field name="{$childName}_unit_value"><xslout:value-of select='indivodoc:{$childName}/indivodoc:unit/@value' /></Field>
                      </xslout:if>
                      <xslout:if test="indivodoc:{$childName}/indivodoc:unit/@abbrev">
                        <Field name="{$childName}_unit_abbrev"><xslout:value-of select='indivodoc:{$childName}/indivodoc:unit/@abbrev' /></Field>
                      </xslout:if>
                    </xslout:if>
                  </xslout:if>
                </xsl:when>

                <xsl:when test="(@type = 'indivo:CollaboRhythmValueAndUnit' or @type = 'indivo:ValueAndUnit')">
                  <xslout:if test="indivodoc:{$childName}/indivodoc:value">
                    <Field name="{$childName}_value"><xslout:value-of select='indivodoc:{$childName}/indivodoc:value'/></Field>
                  </xslout:if>
                  <xslout:if test="indivodoc:{$childName}/indivodoc:textValue">
                    <Field name="{$childName}_textValue"><xslout:value-of select='indivodoc:{$childName}/indivodoc:textValue' /></Field>
                  </xslout:if>
                  <xslout:if test="indivodoc:{$childName}/indivodoc:unit">
                    <Field name="{$childName}_unit_text"><xslout:value-of select='indivodoc:{$childName}/indivodoc:unit/text()' /></Field>
                    <xslout:if test="indivodoc:{$childName}/indivodoc:unit/@type">
                      <Field name="{$childName}_unit_type"><xslout:value-of select='indivodoc:{$childName}/indivodoc:unit/@type'/></Field>
                    </xslout:if>
                    <xslout:if test="indivodoc:{$childName}/indivodoc:unit/@value">
                      <Field name="{$childName}_unit_value"><xslout:value-of select='indivodoc:{$childName}/indivodoc:unit/@value' /></Field>
                    </xslout:if>
                    <xslout:if test="indivodoc:{$childName}/indivodoc:unit/@abbrev">
                      <Field name="{$childName}_unit_abbrev"><xslout:value-of select='indivodoc:{$childName}/indivodoc:unit/@abbrev' /></Field>
                    </xslout:if>
                  </xslout:if>
                </xsl:when>

                <xsl:when test="@type = 'indivo:RecurrenceRule' and @minOccurs='0'">
                  <xslout:if test="indivodoc:{$childName}">
                    <Field name="{$childName}_frequency"><xslout:value-of select='indivodoc:{$childName}/indivodoc:frequency/text()'/></Field>
                    <xslout:if test="indivodoc:{$childName}/indivodoc:interval">
                      <Field name="{$childName}_interval"><xslout:value-of select='indivodoc:{$childName}/indivodoc:interval/text()' /></Field>
                    </xslout:if>
                    <xslout:if test="indivodoc:{$childName}/indivodoc:count">
                      <Field name="{$childName}_count"><xslout:value-of select='indivodoc:{$childName}/indivodoc:count/text()' /></Field>
                    </xslout:if>
                  </xslout:if>
                </xsl:when>

                <xsl:when test="@type = 'indivo:RecurrenceRule'">
                  <Field name="{$childName}_frequency"><xslout:value-of select='indivodoc:{$childName}/indivodoc:frequency/text()'/></Field>
                  <xslout:if test="indivodoc:{$childName}/indivodoc:interval">
                    <Field name="{$childName}_interval"><xslout:value-of select='indivodoc:{$childName}/indivodoc:interval/text()' /></Field>
                  </xslout:if>
                  <xslout:if test="indivodoc:{$childName}/indivodoc:count">
                    <Field name="{$childName}_count"><xslout:value-of select='indivodoc:{$childName}/indivodoc:count/text()' /></Field>
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