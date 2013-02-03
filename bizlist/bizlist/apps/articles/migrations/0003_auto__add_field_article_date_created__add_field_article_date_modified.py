# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Article.date_created'
        db.add_column('articles_article', 'date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 2, 2, 20, 37, 36, 125794), blank=True), keep_default=False)

        # Adding field 'Article.date_modified'
        db.add_column('articles_article', 'date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 2, 2, 20, 37, 39, 764826), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Article.date_created'
        db.delete_column('articles_article', 'date_created')

        # Deleting field 'Article.date_modified'
        db.delete_column('articles_article', 'date_modified')


    models = {
        'articles.article': {
            'Meta': {'object_name': 'Article'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['articles']
