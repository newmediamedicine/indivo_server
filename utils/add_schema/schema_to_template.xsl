<?xml version='1.0' encoding='ISO-8859-1'?>
<xsl:stylesheet version='1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'
                xmlns:indivodoc="http://indivo.org/vocab/xml/documents#" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xsl:output method="text" indent="no"/>
  <xsl:template match="xs:schema">
    <xsl:variable name="name" select="xs:element/@name"/>
{% load template_utils %}
&lt;<xsl:value-of select="$name"/> xmlns="http://indivo.org/vocab/xml/documents#"&gt;
      <xsl:for-each select="xs:complexType[@name=$name]/xs:sequence/xs:element">
        <xsl:variable name="childName" select="@name"/>
        <xsl:choose>
          <xsl:when test="(@type = 'indivo:CollaboRhythmCodedValue' or @type = 'indivo:CodedValue')">
            <xsl:if test="@minOccurs='0'">
              {% if fobj.<xsl:value-of select="$childName"/>_text or
                fobj.<xsl:value-of select="$childName"/>_type or
                fobj.<xsl:value-of select="$childName"/>_value or
                fobj.<xsl:value-of select="$childName"/>_abbrev %}
            </xsl:if>
            &lt;<xsl:value-of select="$childName"/>
            {% if fobj.<xsl:value-of select="$childName"/>_type %} type="{{ fobj.<xsl:value-of select="$childName"/>_type }}"{% endif %}
            {% if fobj.<xsl:value-of select="$childName"/>_value %} value="{{ fobj.<xsl:value-of select="$childName"/>_value }}"{% endif %}
            {% if fobj.<xsl:value-of select="$childName"/>_abbrev %} abbrev="{{ fobj.<xsl:value-of select="$childName"/>_abbrev }}"{% endif %}
            &gt;
            {% if fobj.<xsl:value-of select="$childName"/>_text %}{{ fobj.<xsl:value-of select="$childName"/>_text }}{% endif %}
            &lt;/<xsl:value-of select="$childName"/>&gt;
            <xsl:if test="@minOccurs='0'">{% endif %}</xsl:if>
          </xsl:when>
          <xsl:when test="(@type = 'indivo:CollaboRhythmValueAndUnit' or @type = 'indivo:ValueAndUnit')">
            <xsl:if test="@minOccurs='0'">
              {% if fobj.<xsl:value-of select="$childName"/>_value or
              fobj.<xsl:value-of select="$childName"/>_textValue%}
            </xsl:if>
            &lt;<xsl:value-of select="$childName"/>&gt;

            {% if fobj.<xsl:value-of select="$childName"/>_value %} &lt;value&gt;{{ fobj.<xsl:value-of select="$childName"/>_value }}&lt;/value&gt;{% endif %}
            {% if fobj.<xsl:value-of select="$childName"/>_textValue %} &lt;textValue&gt;{{ fobj.<xsl:value-of select="$childName"/>_textValue }}&lt;/textValue&gt;{% endif %}
            {% if fobj.<xsl:value-of select="$childName"/>_unit_text or fobj.<xsl:value-of select="$childName"/>_unit_type or fobj.<xsl:value-of select="$childName"/>_unit_value or fobj.<xsl:value-of select="$childName"/>_unit_abbrev %}

              <xsl:if test="unit/@minOccurs='0'">
                {% if fobj.<xsl:value-of select="$childName"/>_unit_text or
                fobj.<xsl:value-of select="$childName"/>_unit_type or
                fobj.<xsl:value-of select="$childName"/>_unit_value or
                fobj.<xsl:value-of select="$childName"/>_unit_abbrev %}
              </xsl:if>
              &lt;unit
              {% if fobj.<xsl:value-of select="$childName"/>_unit_type %} type="{{ fobj.<xsl:value-of select="$childName"/>_unit_type }}"{% endif %}
              {% if fobj.<xsl:value-of select="$childName"/>_unit_value %} value="{{ fobj.<xsl:value-of select="$childName"/>_unit_value }}"{% endif %}
              {% if fobj.<xsl:value-of select="$childName"/>_unit_abbrev %} abbrev="{{ fobj.<xsl:value-of select="$childName"/>_unit_abbrev }}"{% endif %}
              &gt;
              {% if fobj.<xsl:value-of select="$childName"/>_unit_text %}{{ fobj.<xsl:value-of select="$childName"/>_unit_text }}{% endif %}
              &lt;unit/&gt;
              <xsl:if test="@minOccurs='0'">{% endif %}</xsl:if>

            {% endif %}
            &lt;/<xsl:value-of select="$childName"/>&gt;
            <xsl:if test="@minOccurs='0'">{% endif %}</xsl:if>
          </xsl:when>
          <xsl:when test="@type = 'indivo:RecurrenceRule'">
            <xsl:if test="@minOccurs='0'">
              {% if fobj.<xsl:value-of select="$childName"/>_frequency %}
            </xsl:if>
            &lt;<xsl:value-of select="$childName"/>&gt;
            &lt;frequency&gt;{{ fobj.<xsl:value-of select="$childName"/>_frequency }}&lt;/value&gt;
            {% if fobj.<xsl:value-of select="$childName"/>_interval %} &lt;interval&gt;{{ fobj.<xsl:value-of select="$childName"/>_interval }}&lt;/interval&gt;{% endif %}
            {% if fobj.<xsl:value-of select="$childName"/>_count %} &lt;count&gt;{{ fobj.<xsl:value-of select="$childName"/>_count }}&lt;/count&gt;{% endif %}
            &lt;/<xsl:value-of select="$childName"/>&gt;
            <xsl:if test="@minOccurs='0'">{% endif %}</xsl:if>
          </xsl:when>
          <xsl:otherwise>
            <xsl:if test="@minOccurs='0'">  {% if fobj.<xsl:value-of select="$childName"/> %}</xsl:if>
  &lt;<xsl:value-of select="$childName"/>&gt;{{ fobj.<xsl:value-of select="$childName"/><xsl:if test="@type = 'xs:dateTime'">|format_iso8601_datetime</xsl:if><xsl:if test="@type = 'xs:date'">|format_iso8601_date</xsl:if><xsl:if test="@type = 'xs:boolean'">|lower</xsl:if> }}&lt;/<xsl:value-of select="$childName"/>&gt;
  <xsl:if test="@minOccurs='0'">{% endif %}</xsl:if>
          </xsl:otherwise>
        </xsl:choose>
        <xsl:text>&#10;</xsl:text>
      </xsl:for-each>
&lt;/<xsl:value-of select="$name"/>&gt;
  </xsl:template>
</xsl:stylesheet>
