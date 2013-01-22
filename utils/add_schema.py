#!/usr/bin/python

"""
.. module:: utils.add_schema
   :synopsis: Script for adding a contributed schema

.. moduleauthor:: Scott Gilroy <sgilroy@mit.edu>

"""

# Set up the Django environment
import sys
import os
from django.core import management
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))
from django.db import connection, DatabaseError, IntegrityError

from optparse import OptionParser
import subprocess
import libxml2
import libxslt
from lxml import etree
from pwd import getpwnam
from grp import getgrnam
import stat

def transform_file1(inputPath, transformPath, outputPath):
    outputDir = os.path.dirname(outputPath)
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    stylesheetArgs = {} # optional transform args
    styleDoc = libxml2.parseFile(transformPath) # <xml ...xsl:stylesheet >
    style = libxslt.parseStylesheetDoc(styleDoc)

    doc = libxml2.parseFile(inputPath) # <xml input file>
    result = style.applyStylesheet(doc,stylesheetArgs)
    res = style.saveResultToFilename(outputPath, result, 0)
    style.freeStylesheet()
    doc.freeDoc()
    result.freeDoc()

    print open(outputPath).read()

    return res

def transform_file(inputPath, transformPath, outputPath, match=None, replace=None):
    outputDir = os.path.dirname(outputPath)
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
        os.chown(outputDir, getpwnam('www-data').pw_uid, getgrnam('developers').gr_gid)
        os.chmod(outputDir, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH)

    xml_input = etree.XML(open(inputPath, 'r').read())
    xslt_root = etree.XML(open(transformPath, 'r').read())
    transform = etree.XSLT(xslt_root)
    outputFile = open(outputPath, 'w')
    transformResult = str(transform(xml_input))
    if match is not None:
        transformResult = transformResult.replace(match, replace)
    outputFile.write(transformResult)
    outputFile.close()

    os.chown(outputPath, getpwnam('www-data').pw_uid, getgrnam('developers').gr_gid)
    os.chmod(outputPath, stat.S_IREAD | stat.S_IWRITE | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH)

    print open(outputPath).read()

    return

# Parse commandline Arguments
usage = ''' %prog [options]

Add a new schema to Indivo, generating necessary model, transform, and report files.
Source schema xsd file should be placed in indivo_server/indivo/contrib/<model_name>/schema.xsd

Some of the commands (i.e. dropping and creating the database)
require authentication to the underlying database. If you are prompted
for a password, use the password for your database user (the same one you
specified in settings.py)'''

parser = OptionParser(usage=usage)
parser.add_option("-s",
    dest="schema", default="myschema",
    help="Add the specified schema.")

(options, args) = parser.parse_args()

## Prompt for confirmation--we are about to trash a database, after all
#confirm = raw_input("""You have requested to auto-generate the supporting files for schema %r
#Are you sure you want to do this?
#
#    Type 'yes' to continue, or 'no' to cancel: """ % options.schema)
#
#if confirm != 'yes':
#    print "Add cancelled."
#
#else:
print "Adding schema %r..." % options.schema

schemaPath = "indivo/schemas/data/contrib/" + options.schema + "/schema.xsd"
modelPath = "indivo/data_models/contrib/" + options.schema + "/model.py"
extraPath = "indivo/data_models/contrib/" + options.schema + "/extra.py"

transformPath = "indivo/schemas/data/contrib/" + options.schema + "/transform.xsl"
templatePath = "indivo/templates/reports/" + options.schema + ".xml"

examplePath = "indivo/schemas/data/contrib/" + options.schema + "/" + options.schema + ".xml"

if os.path.isfile(schemaPath):
    print "Path found: " + schemaPath

    transform_file(schemaPath, "utils/add_schema/schema_to_model.xsl", modelPath)
    transform_file(schemaPath, "utils/add_schema/schema_to_extra.xsl", extraPath)
    transform_file(schemaPath, "utils/add_schema/schema_to_transform.xsl", transformPath, "xslout", "xsl")
    transform_file(schemaPath, "utils/add_schema/schema_to_template.xsl", templatePath)

else:
    print "Not found: " + schemaPath