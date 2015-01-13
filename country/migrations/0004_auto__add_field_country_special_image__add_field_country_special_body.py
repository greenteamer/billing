# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Country.special_image'
        db.add_column(u'country_country', 'special_image',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Country.special_body'
        db.add_column(u'country_country', 'special_body',
                      self.gf('ckeditor.fields.RichTextField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Country.special_image'
        db.delete_column(u'country_country', 'special_image')

        # Deleting field 'Country.special_body'
        db.delete_column(u'country_country', 'special_body')


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
        u'country.countryimage': {
            'Meta': {'object_name': 'CountryImage'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['country.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['country']