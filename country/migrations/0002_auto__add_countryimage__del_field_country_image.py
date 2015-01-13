# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CountryImage'
        db.create_table(u'country_countryimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['country.Country'])),
        ))
        db.send_create_signal(u'country', ['CountryImage'])

        # Deleting field 'Country.image'
        db.delete_column(u'country_country', 'image')


    def backwards(self, orm):
        # Deleting model 'CountryImage'
        db.delete_table(u'country_countryimage')

        # Adding field 'Country.image'
        db.add_column(u'country_country', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='default.jpg', max_length=100),
                      keep_default=False)


    models = {
        u'country.country': {
            'Meta': {'object_name': 'Country'},
            'body': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'})
        },
        u'country.countryimage': {
            'Meta': {'object_name': 'CountryImage'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['country.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['country']