# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WildfireUpdate.fire_name'
        db.add_column('calfire_tracker_wildfireupdate', 'fire_name',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calfire_tracker.CalWildfire'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field fire_name on 'WildfireUpdate'
        db.delete_table('calfire_tracker_wildfireupdate_fire_name')


    def backwards(self, orm):
        # Deleting field 'WildfireUpdate.fire_name'
        db.delete_column('calfire_tracker_wildfireupdate', 'fire_name_id')

        # Adding M2M table for field fire_name on 'WildfireUpdate'
        db.create_table('calfire_tracker_wildfireupdate_fire_name', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('wildfireupdate', models.ForeignKey(orm['calfire_tracker.wildfireupdate'], null=False)),
            ('calwildfire', models.ForeignKey(orm['calfire_tracker.calwildfire'], null=False))
        ))
        db.create_unique('calfire_tracker_wildfireupdate_fire_name', ['wildfireupdate_id', 'calwildfire_id'])


    models = {
        'calfire_tracker.calwildfire': {
            'Meta': {'object_name': 'CalWildfire'},
            'acres_burned': ('django.db.models.fields.IntegerField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'administrative_unit': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'asset_host_image_id': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'cause': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'computed_location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'conditions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'containment_percent': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'cooperating_agencies': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'created_fire_id': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'current_situation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'damage_assessment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_time_started': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'evacuations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fire_name': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'fire_slug': ('django.db.models.fields.SlugField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'injuries': ('django.db.models.fields.CharField', [], {'max_length': '2024', 'null': 'True', 'blank': 'True'}),
            'last_scraped': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'location_geocode_error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location_latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location_longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'more_info': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phone_numbers': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'promoted_fire': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'road_closures': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'structures_destroyed': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'structures_threatened': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'total_airtankers': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'total_dozers': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'total_fire_crews': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'total_fire_engines': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'total_fire_personnel': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'total_helicopters': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'total_water_tenders': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'training': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'twitter_hashtag': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'})
        },
        'calfire_tracker.wildfireupdate': {
            'Meta': {'object_name': 'WildfireUpdate'},
            'date_time_update': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fire_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['calfire_tracker.CalWildfire']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'update_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['calfire_tracker']