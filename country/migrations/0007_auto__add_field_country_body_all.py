# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Country.body_all'
        db.add_column(u'country_country', 'body_all',
                      self.gf('ckeditor.fields.RichTextField')(default='default'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Country.body_all'
        db.delete_column(u'country_country', 'body_all')


    models = {
        u'country.country': {
            'Meta': {'object_name': 'Country'},
            'body': ('ckeditor.fields.RichTextField', [], {}),
            'body_all': ('ckeditor.fields.RichTextField', [], {}),
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
        u'country.countryimage': {
            'Meta': {'object_name': 'CountryImage'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['country.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['country']