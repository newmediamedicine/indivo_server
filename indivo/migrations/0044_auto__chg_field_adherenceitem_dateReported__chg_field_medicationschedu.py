# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'AdherenceItem.dateReported'
        db.alter_column('indivo_adherenceitem', 'dateReported', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'MedicationScheduleItem.dateStart'
        db.alter_column('indivo_medicationscheduleitem', 'dateStart', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'MedicationScheduleItem.dateScheduled'
        db.alter_column('indivo_medicationscheduleitem', 'dateScheduled', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'MedicationScheduleItem.dateEnd'
        db.alter_column('indivo_medicationscheduleitem', 'dateEnd', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'HealthActionSchedule.dateStart'
        db.alter_column('indivo_healthactionschedule', 'dateStart', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'HealthActionSchedule.dateScheduled'
        db.alter_column('indivo_healthactionschedule', 'dateScheduled', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'HealthActionSchedule.dateEnd'
        db.alter_column('indivo_healthactionschedule', 'dateEnd', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'CollaboRhythmVitalSign.dateMeasuredEnd'
        db.alter_column('indivo_collaborhythmvitalsign', 'dateMeasuredEnd', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'CollaboRhythmVitalSign.dateMeasuredStart'
        db.alter_column('indivo_collaborhythmvitalsign', 'dateMeasuredStart', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'MedicationAdministration.dateAdministered'
        db.alter_column('indivo_medicationadministration', 'dateAdministered', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'MedicationAdministration.dateReported'
        db.alter_column('indivo_medicationadministration', 'dateReported', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'AdherenceItem.dateReported'
        db.alter_column('indivo_adherenceitem', 'dateReported', self.gf('django.db.models.fields.DateField')())

        # Changing field 'MedicationScheduleItem.dateStart'
        db.alter_column('indivo_medicationscheduleitem', 'dateStart', self.gf('django.db.models.fields.DateField')())

        # Changing field 'MedicationScheduleItem.dateScheduled'
        db.alter_column('indivo_medicationscheduleitem', 'dateScheduled', self.gf('django.db.models.fields.DateField')())

        # Changing field 'MedicationScheduleItem.dateEnd'
        db.alter_column('indivo_medicationscheduleitem', 'dateEnd', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'HealthActionSchedule.dateStart'
        db.alter_column('indivo_healthactionschedule', 'dateStart', self.gf('django.db.models.fields.DateField')())

        # Changing field 'HealthActionSchedule.dateScheduled'
        db.alter_column('indivo_healthactionschedule', 'dateScheduled', self.gf('django.db.models.fields.DateField')())

        # Changing field 'HealthActionSchedule.dateEnd'
        db.alter_column('indivo_healthactionschedule', 'dateEnd', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'CollaboRhythmVitalSign.dateMeasuredEnd'
        db.alter_column('indivo_collaborhythmvitalsign', 'dateMeasuredEnd', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'CollaboRhythmVitalSign.dateMeasuredStart'
        db.alter_column('indivo_collaborhythmvitalsign', 'dateMeasuredStart', self.gf('django.db.models.fields.DateField')())

        # Changing field 'MedicationAdministration.dateAdministered'
        db.alter_column('indivo_medicationadministration', 'dateAdministered', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'MedicationAdministration.dateReported'
        db.alter_column('indivo_medicationadministration', 'dateReported', self.gf('django.db.models.fields.DateField')())

    models = {
        'indivo.accesstoken': {
            'Meta': {'object_name': 'AccessToken', '_ormbases': ['indivo.Principal']},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']", 'null': 'True'}),
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']", 'null': 'True'}),
            'connect_auth_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expires_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'}),
            'share': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.PHAShare']"}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'token_secret': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'indivo.account': {
            'Meta': {'object_name': 'Account', '_ormbases': ['indivo.Principal']},
            'account': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'}),
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'failed_login_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'last_failed_login_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_login_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_state_change': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'primary_secret': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'secondary_secret': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'uninitialized'", 'max_length': '50'}),
            'total_login_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'indivo.accountauthsystem': {
            'Meta': {'unique_together': "(('auth_system', 'account'), ('auth_system', 'username'))", 'object_name': 'AccountAuthSystem'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'auth_systems'", 'to': "orm['indivo.Account']"}),
            'auth_parameters': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'auth_system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.AuthSystem']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accountauthsystem_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user_attributes': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'indivo.accountfullshare': {
            'Meta': {'unique_together': "(('record', 'with_account'),)", 'object_name': 'AccountFullShare'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accountfullshare_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fullshares'", 'to': "orm['indivo.Record']"}),
            'role_label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'with_account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fullshares_to'", 'to': "orm['indivo.Account']"})
        },
        'indivo.adherenceitem': {
            'Meta': {'object_name': 'AdherenceItem', '_ormbases': ['indivo.Fact']},
            'adherence': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dateReported': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nonadherenceReason': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'recurrenceIndex': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reportedBy': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'indivo.allergy': {
            'Meta': {'object_name': 'Allergy', '_ormbases': ['indivo.Fact']},
            'allergic_reaction_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'allergic_reaction_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'allergic_reaction_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'category_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'category_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'category_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'drug_allergen_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drug_allergen_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drug_allergen_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drug_class_allergen_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drug_class_allergen_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drug_class_allergen_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'food_allergen_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'food_allergen_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'food_allergen_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'severity_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'severity_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'severity_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'indivo.allergyexclusion': {
            'Meta': {'object_name': 'AllergyExclusion', '_ormbases': ['indivo.Fact']},
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'indivo.audit': {
            'Meta': {'object_name': 'Audit'},
            'carenet_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'document_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'effective_principal_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'pha_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'proxied_by_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'record_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'req_domain': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'req_headers': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'req_ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True'}),
            'req_method': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'req_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'request_successful': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resp_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'resp_headers': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'view_func': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'indivo.authsystem': {
            'Meta': {'object_name': 'AuthSystem'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'authsystem_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'internal_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'indivo.carenet': {
            'Meta': {'unique_together': "(('name', 'record'),)", 'object_name': 'Carenet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenet_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']"})
        },
        'indivo.carenetaccount': {
            'Meta': {'unique_together': "(('carenet', 'account'),)", 'object_name': 'CarenetAccount'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']"}),
            'can_write': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenetaccount_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'indivo.carenetautoshare': {
            'Meta': {'unique_together': "(('carenet', 'record', 'type'),)", 'object_name': 'CarenetAutoshare'},
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenetautoshare_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.DocumentSchema']", 'null': 'True'})
        },
        'indivo.carenetdocument': {
            'Meta': {'unique_together': "(('carenet', 'document'),)", 'object_name': 'CarenetDocument'},
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenetdocument_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'share_p': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'indivo.carenetpha': {
            'Meta': {'unique_together': "(('carenet', 'pha'),)", 'object_name': 'CarenetPHA'},
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenetpha_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'pha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.PHA']"})
        },
        'indivo.collaborhythmvitalsign': {
            'Meta': {'object_name': 'CollaboRhythmVitalSign', '_ormbases': ['indivo.Fact']},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dateMeasuredEnd': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'dateMeasuredStart': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'measuredBy': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_textValue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_unit_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '22', 'decimal_places': '10', 'blank': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'technique': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'indivo.demographics': {
            'Meta': {'object_name': 'Demographics'},
            'adr_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adr_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adr_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'adr_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adr_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bday': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_family': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_given': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_middle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_suffix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'preferred_language': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tel_1_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tel_1_preferred_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tel_1_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'tel_2_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tel_2_preferred_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tel_2_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'indivo.document': {
            'Meta': {'unique_together': "(('record', 'external_id'),)", 'object_name': 'Document'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'content_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'document_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'digest': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'fqn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'mime_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'nevershare': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'original': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'document_thread'", 'null': 'True', 'to': "orm['indivo.Document']"}),
            'pha': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pha_document'", 'null': 'True', 'to': "orm['indivo.PHA']"}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documents'", 'null': 'True', 'to': "orm['indivo.Record']"}),
            'replaced_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'document_replaced'", 'null': 'True', 'to': "orm['indivo.Document']"}),
            'replaces': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']", 'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['indivo.StatusName']"}),
            'suppressed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'suppressed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Principal']", 'null': 'True'})
        },
        'indivo.documentrels': {
            'Meta': {'object_name': 'DocumentRels'},
            'document_0': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rels_as_doc_0'", 'to': "orm['indivo.Document']"}),
            'document_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rels_as_doc_1'", 'to': "orm['indivo.Document']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.DocumentSchema']"})
        },
        'indivo.documentschema': {
            'Meta': {'object_name': 'DocumentSchema'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documentschema_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'internal_p': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'stylesheet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stylesheet'", 'null': 'True', 'to': "orm['indivo.Document']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'indivo.documentstatushistory': {
            'Meta': {'object_name': 'DocumentStatusHistory'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documentstatushistory_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'document': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'effective_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'proxied_by_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'reason': ('django.db.models.fields.TextField', [], {}),
            'record': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.StatusName']"})
        },
        'indivo.encounter': {
            'Meta': {'object_name': 'Encounter', '_ormbases': ['indivo.Fact']},
            'encounterType_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'encounterType_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'encounterType_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'endDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'facility_adr_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facility_adr_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facility_adr_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'facility_adr_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facility_adr_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facility_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'provider_adr_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_adr_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_adr_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'provider_adr_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_adr_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_bday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'provider_dea_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_family': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_given': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_middle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_suffix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_npi_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_preferred_language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_race': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_tel_1_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'provider_tel_1_preferred_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'provider_tel_1_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'provider_tel_2_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'provider_tel_2_preferred_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'provider_tel_2_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'startDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'indivo.equipment': {
            'Meta': {'object_name': 'Equipment', '_ormbases': ['indivo.Fact']},
            'date_started': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_stopped': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        'indivo.fact': {
            'Meta': {'object_name': 'Fact'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']", 'null': 'True', 'blank': 'True'})
        },
        'indivo.fill': {
            'Meta': {'object_name': 'Fill', '_ormbases': ['indivo.Fact']},
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'dispenseDaysSupply': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'medication': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fulfillments'", 'null': 'True', 'to': "orm['indivo.Medication']"}),
            'pbm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pharmacy_adr_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pharmacy_adr_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pharmacy_adr_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'pharmacy_adr_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pharmacy_adr_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pharmacy_ncpdpid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pharmacy_org': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_adr_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_adr_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_adr_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'provider_adr_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_adr_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_bday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'provider_dea_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_family': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_given': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_middle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_suffix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_npi_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_preferred_language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_race': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_tel_1_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'provider_tel_1_preferred_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'provider_tel_1_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'provider_tel_2_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'provider_tel_2_preferred_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'provider_tel_2_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'quantityDispensed_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantityDispensed_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'indivo.healthactionoccurrence': {
            'Meta': {'object_name': 'HealthActionOccurrence', '_ormbases': ['indivo.Fact']},
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'recurrenceIndex': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'indivo.healthactionplan': {
            'Meta': {'object_name': 'HealthActionPlan', '_ormbases': ['indivo.Fact']},
            'actions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dateExpires': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'datePlanned': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'indication': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'instructions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'planType': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'plannedBy': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'system_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'system_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'system_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'system_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'indivo.healthactionschedule': {
            'Meta': {'object_name': 'HealthActionSchedule', '_ormbases': ['indivo.Fact']},
            'dateEnd': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'dateScheduled': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'dateStart': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'recurrenceRule_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recurrenceRule_frequency': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'recurrenceRule_interval': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scheduledBy': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'indivo.immunization': {
            'Meta': {'object_name': 'Immunization', '_ormbases': ['indivo.Fact']},
            'administration_status_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'administration_status_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'administration_status_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'product_class_2_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_class_2_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_class_2_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_class_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_class_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_class_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'product_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'refusal_reason_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'refusal_reason_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'refusal_reason_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'indivo.labresult': {
            'Meta': {'object_name': 'LabResult', '_ormbases': ['indivo.Fact']},
            'abnormal_interpretation_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'abnormal_interpretation_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'abnormal_interpretation_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'accession_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'collected_by_name_family': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_name_given': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_name_middle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_name_prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_name_suffix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_org_adr_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_org_adr_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_org_adr_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'collected_by_org_adr_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_org_adr_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_org_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_role': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'narrative_result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_non_critical_range_max_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_non_critical_range_max_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_non_critical_range_min_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_non_critical_range_min_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_normal_range_max_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_normal_range_max_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_normal_range_min_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_normal_range_min_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_value_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_value_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'test_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'test_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'test_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'indivo.machineapp': {
            'Meta': {'object_name': 'MachineApp'},
            'app_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'indivo_version': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'})
        },
        'indivo.measurement': {
            'Meta': {'object_name': 'Measurement', '_ormbases': ['indivo.Fact']},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {'blank': 'True'})
        },
        'indivo.medication': {
            'Meta': {'object_name': 'Medication', '_ormbases': ['indivo.Fact']},
            'drugName_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'drugName_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drugName_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'endDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'frequency_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'frequency_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'instructions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provenance_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provenance_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provenance_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantity_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantity_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'startDate': ('django.db.models.fields.DateField', [], {'null': 'True'})
        },
        'indivo.medicationadministration': {
            'Meta': {'object_name': 'MedicationAdministration', '_ormbases': ['indivo.Fact']},
            'amountAdministered_textValue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountAdministered_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountAdministered_unit_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountAdministered_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountAdministered_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountAdministered_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '22', 'decimal_places': '10', 'blank': 'True'}),
            'amountRemaining_textValue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountRemaining_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountRemaining_unit_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountRemaining_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountRemaining_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountRemaining_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '22', 'decimal_places': '10', 'blank': 'True'}),
            'dateAdministered': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'dateReported': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'reportedBy': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'indivo.medicationfill': {
            'Meta': {'object_name': 'MedicationFill', '_ormbases': ['indivo.Fact']},
            'amountFilled_textValue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountFilled_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountFilled_unit_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountFilled_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountFilled_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountFilled_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '22', 'decimal_places': '10', 'blank': 'True'}),
            'dateFilled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'fillSequenceNumber': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'filledBy': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'instructions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'lotNumber': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ndc_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ndc_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ndc_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ndc_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'refillsRemaining': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'indivo.medicationorder': {
            'Meta': {'object_name': 'MedicationOrder', '_ormbases': ['indivo.Fact']},
            'amountOrdered_textValue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountOrdered_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountOrdered_unit_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountOrdered_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountOrdered_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amountOrdered_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '22', 'decimal_places': '10', 'blank': 'True'}),
            'dateExpires': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'dateOrdered': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'indication': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'instructions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'orderType': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'orderedBy': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'refills': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'substitutionPermitted': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'indivo.medicationscheduleitem': {
            'Meta': {'object_name': 'MedicationScheduleItem', '_ormbases': ['indivo.Fact']},
            'dateEnd': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'dateScheduled': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'dateStart': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'dose_textValue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dose_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dose_unit_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dose_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dose_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dose_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '22', 'decimal_places': '10', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'recurrenceRule_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recurrenceRule_frequency': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'recurrenceRule_interval': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scheduledBy': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'indivo.message': {
            'Meta': {'unique_together': "(('account', 'external_identifier', 'sender'),)", 'object_name': 'Message'},
            'about_record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']", 'null': 'True'}),
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']"}),
            'archived_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'body_type': ('django.db.models.fields.CharField', [], {'default': "'plaintext'", 'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'external_identifier': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'num_attachments': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'read_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'received_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_as_recipient'", 'to': "orm['indivo.Principal']"}),
            'response_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_responses'", 'null': 'True', 'to': "orm['indivo.Message']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_as_sender'", 'to': "orm['indivo.Principal']"}),
            'severity': ('django.db.models.fields.CharField', [], {'default': "'low'", 'max_length': '100'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indivo.messageattachment': {
            'Meta': {'unique_together': "(('message', 'attachment_num'),)", 'object_name': 'MessageAttachment'},
            'attachment_num': ('django.db.models.fields.IntegerField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messageattachment_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Message']"}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'saved_to_document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']", 'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'indivo.nonce': {
            'Meta': {'unique_together': "(('nonce', 'oauth_type'),)", 'object_name': 'Nonce'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nonce': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'oauth_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        'indivo.notification': {
            'Meta': {'object_name': 'Notification'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']"}),
            'app_url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notification_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']", 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']", 'null': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notifications_sent_by'", 'to': "orm['indivo.Principal']"})
        },
        'indivo.nouser': {
            'Meta': {'object_name': 'NoUser', '_ormbases': ['indivo.Principal']},
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'})
        },
        'indivo.pha': {
            'Meta': {'object_name': 'PHA'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'autonomous_reason': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'callback_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'frameable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_ui': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'icon_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'indivo_version': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'is_autonomous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'}),
            'requirements': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'start_url_template': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'})
        },
        'indivo.phashare': {
            'Meta': {'unique_together': "(('record', 'with_pha'),)", 'object_name': 'PHAShare'},
            'authorized_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'authorized_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shares_authorized_by'", 'null': 'True', 'to': "orm['indivo.Account']"}),
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']", 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phashare_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pha_shares'", 'to': "orm['indivo.Record']"}),
            'with_pha': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pha_shares_to'", 'to': "orm['indivo.PHA']"})
        },
        'indivo.principal': {
            'Meta': {'object_name': 'Principal'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'principal_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indivo.problem': {
            'Meta': {'object_name': 'Problem', '_ormbases': ['indivo.Fact']},
            'endDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'startDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'indivo.procedure': {
            'Meta': {'object_name': 'Procedure', '_ormbases': ['indivo.Fact']},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_performed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'provider_institution': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'indivo.record': {
            'Meta': {'object_name': 'Record'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'record_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'demographics': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Demographics']", 'unique': 'True', 'null': 'True'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'records_owned_by'", 'null': 'True', 'to': "orm['indivo.Principal']"})
        },
        'indivo.recordnotificationroute': {
            'Meta': {'unique_together': "(('account', 'record'),)", 'object_name': 'RecordNotificationRoute'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recordnotificationroute_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notification_routes'", 'to': "orm['indivo.Record']"})
        },
        'indivo.reqtoken': {
            'Meta': {'object_name': 'ReqToken', '_ormbases': ['indivo.Principal']},
            'authorized_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'authorized_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']", 'null': 'True'}),
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']", 'null': 'True'}),
            'oauth_callback': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'pha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.PHA']"}),
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']", 'null': 'True'}),
            'share': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.PHAShare']", 'null': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'token_secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'verifier': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'indivo.sessionrequesttoken': {
            'Meta': {'object_name': 'SessionRequestToken'},
            'approved_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sessionrequesttoken_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']", 'null': 'True'})
        },
        'indivo.sessiontoken': {
            'Meta': {'object_name': 'SessionToken'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sessiontoken_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'expires_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']", 'null': 'True'})
        },
        'indivo.simpleclinicalnote': {
            'Meta': {'object_name': 'SimpleClinicalNote', '_ormbases': ['indivo.Fact']},
            'chief_complaint': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_visit': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'finalized_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'provider_institution': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'signed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'specialty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'specialty_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'specialty_type': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'specialty_value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'visit_location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'visit_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'visit_type_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'visit_type_type': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'visit_type_value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        'indivo.statusname': {
            'Meta': {'object_name': 'StatusName'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        'indivo.vitalsigns': {
            'Meta': {'object_name': 'VitalSigns', '_ormbases': ['indivo.Fact']},
            'bmi_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bmi_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bmi_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bmi_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bmi_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bp_diastolic_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_diastolic_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_diastolic_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_diastolic_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_diastolic_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bp_method_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_method_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_method_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_position_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_position_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_position_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_site_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_site_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_site_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_systolic_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_systolic_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_systolic_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_systolic_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_systolic_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'encounter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Encounter']", 'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'heart_rate_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'heart_rate_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'heart_rate_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'heart_rate_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'heart_rate_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'height_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'height_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'height_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'height_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'height_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'oxygen_saturation_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'oxygen_saturation_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'oxygen_saturation_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'oxygen_saturation_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'oxygen_saturation_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'respiratory_rate_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'respiratory_rate_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'respiratory_rate_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'respiratory_rate_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'respiratory_rate_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'temperature_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'temperature_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'temperature_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'temperature_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'temperature_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'weight_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weight_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weight_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weight_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weight_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['indivo']