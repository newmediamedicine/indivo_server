<?xml version="1.0"?>
<xsl:stylesheet xmlns:indivodoc="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" version="1.0">
    <xsl:template match="indivodoc:HealthActionPlan">
        <Models>
            <Model name="HealthActionPlan">

                <!-- name -->
                <Field name="name_text">
                    <xsl:value-of select="indivodoc:name/text()"/>
                </Field>
                <xsl:if test="indivodoc:name/@type">
                    <Field name="name_type">
                        <xsl:value-of select="indivodoc:name/@type"/>
                    </Field>
                </xsl:if>
                <xsl:if test="indivodoc:name/@value">
                    <Field name="name_value">
                        <xsl:value-of select="indivodoc:name/@value"/>
                    </Field>
                </xsl:if>
                <xsl:if test="indivodoc:name/@abbrev">
                    <Field name="name_abbrev">
                        <xsl:value-of select="indivodoc:name/@abbrev"/>
                    </Field>
                </xsl:if>

                <!-- planType -->
                <Field name="planType">
                    <xsl:value-of select="indivodoc:planType/text()"/>
                </Field>

                <!-- plannedBy -->
                <Field name="plannedBy">
                    <xsl:value-of select="indivodoc:plannedBy/text()"/>
                </Field>

                <!-- datePlanned -->
                <Field name="datePlanned">
                    <xsl:value-of select="indivodoc:datePlanned/text()"/>
                </Field>

                <!-- dateExpires -->
                <xsl:if test="indivodoc:dateExpires/value">
                    <Field name="dateExpires">
                        <xsl:value-of select="indivodoc:dateExpires/text()"/>
                    </Field>
                </xsl:if>

                <!-- indication -->
                <Field name="indication">
                    <xsl:value-of select="indivodoc:indication/text()"/>
                </Field>

                <!-- instructions -->
                <Field name="instructions">
                    <xsl:value-of select="indivodoc:instructions/text()"/>
                </Field>

                <!-- system -->
                <Field name="system_text">
                    <xsl:value-of select="indivodoc:system/text()"/>
                </Field>
                <xsl:if test="indivodoc:system/@type">
                    <Field name="system_type">
                        <xsl:value-of select="indivodoc:system/@type"/>
                    </Field>
                </xsl:if>
                <xsl:if test="indivodoc:system/@value">
                    <Field name="system_value">
                        <xsl:value-of select="indivodoc:system/@value"/>
                    </Field>
                </xsl:if>
                <xsl:if test="indivodoc:system/@abbrev">
                    <Field name="system_abbrev">
                        <xsl:value-of select="indivodoc:system/@abbrev"/>
                    </Field>
                </xsl:if>

                <xsl:if test="indivodoc:actions">
                	<Field name="actions">
                        <![CDATA[<xsl:copy-of select="indivodoc:actions/indivodoc:action"/>]]>
                    </Field>
                </xsl:if>

            </Model>
        </Models>
    </xsl:template>

</xsl:stylesheet>