# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'auctions_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal(u'auctions', ['Category'])

        # Adding model 'Item'
        db.create_table(u'auctions_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('belongs_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='auctions', to=orm['auctions.Category'])),
            ('added_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='auctions', to=orm['users.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('condition', self.gf('django.db.models.fields.CharField')(default='new', max_length=5)),
            ('number_of_pieces', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('base_price', self.gf('django.db.models.fields.FloatField')(default=0.01)),
            ('shipping_charges', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('price_difference_in_bids', self.gf('django.db.models.fields.FloatField')(default=0.01)),
            ('auction_start_period', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('auction_end_period', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'auctions', ['Item'])

        # Adding model 'Bid'
        db.create_table(u'auctions_bid', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('made_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bids', to=orm['users.User'])),
            ('made_against', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bids', to=orm['auctions.Item'])),
            ('made_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('bid_price', self.gf('django.db.models.fields.FloatField')()),
            ('is_a_winner', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('awarded_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'auctions', ['Bid'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'auctions_category')

        # Deleting model 'Item'
        db.delete_table(u'auctions_item')

        # Deleting model 'Bid'
        db.delete_table(u'auctions_bid')


    models = {
        u'auctions.bid': {
            'Meta': {'object_name': 'Bid'},
            'awarded_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'bid_price': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_a_winner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'made_against': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bids'", 'to': u"orm['auctions.Item']"}),
            'made_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bids'", 'to': u"orm['users.User']"}),
            'made_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'auctions.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'auctions.item': {
            'Meta': {'object_name': 'Item'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'auctions'", 'to': u"orm['users.User']"}),
            'auction_end_period': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'auction_start_period': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'base_price': ('django.db.models.fields.FloatField', [], {'default': '0.01'}),
            'belongs_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'auctions'", 'to': u"orm['auctions.Category']"}),
            'condition': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '5'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'number_of_pieces': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'price_difference_in_bids': ('django.db.models.fields.FloatField', [], {'default': '0.01'}),
            'shipping_charges': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '20', 'blank': 'True'}),
            'street1': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'street2': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '10', 'blank': 'True'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'born_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "u'U'", 'max_length': '1', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50', 'blank': 'True'}),
            'lives_at': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.Address']", 'unique': 'True', 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        }
    }

    complete_apps = ['auctions']