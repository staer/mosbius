
from south.db import db
from django.db import models
from projects.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Project'
        db.create_table('projects_project', (
            ('id', orm['projects.Project:id']),
            ('title', orm['projects.Project:title']),
            ('slug', orm['projects.Project:slug']),
            ('teaser', orm['projects.Project:teaser']),
            ('body', orm['projects.Project:body']),
            ('start_date', orm['projects.Project:start_date']),
            ('end_date', orm['projects.Project:end_date']),
            ('source_code', orm['projects.Project:source_code']),
        ))
        db.send_create_signal('projects', ['Project'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Project'
        db.delete_table('projects_project')
        
    
    
    models = {
        'projects.project': {
            'body': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'source_code': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'teaser': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['projects']
