# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'feedback_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=30)),
            ('destination', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['country.CountryDestination'])),
        ))
        db.send_create_signal(u'feedback', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'feedback_contact')


    models = {
        u'country.country': {
            'Meta': {'object_name': 'Country'},
            'body': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'special_body': ('ckeditor.fields.RichTextField', [], {'null': 'True'}),
            'special_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'})
        },
        u'country.countrydestination': {
            'Meta': {'object_name': 'CountryDestination'},
            'body': ('ckeditor.fields.RichTextField', [], {}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['country.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'feedback.contact': {
            'Meta': {'object_name': 'Contact'},
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['country.CountryDestination']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '11'})
        }
    }

    complete_apps = ['feedback']