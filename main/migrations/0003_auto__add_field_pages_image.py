# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pages.image'
        db.add_column(u'main_pages', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='default.jpg', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Pages.image'
        db.delete_column(u'main_pages', 'image')


    models = {
        u'main.pages': {
            'Meta': {'object_name': 'Pages'},
            'body': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_aqua': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'})
        }
    }

    complete_apps = ['main']