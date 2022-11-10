# Generated by Django 3.0.3 on 2020-12-04 11:50

import datetime
import dirtyfields.dirtyfields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculationRules',
            fields=[
                ('id', models.UUIDField(db_column='UUID', default=None, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', models.JSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', models.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', models.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', models.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', models.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('calculation_class_name', models.CharField(blank=True, db_column='CalculationsClassName', max_length=255, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True)),
                ('priority', models.IntegerField(blank=True, db_column='Priority', null=True)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
                ('user_created', models.ForeignKey(db_column='UserCreatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='calculationrules_user_created', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(db_column='UserUpdatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='calculationrules_user_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tblCalculationRules',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCalculationRulesDetails',
            fields=[
                ('id', models.UUIDField(db_column='UUID', db_index=True, default=None, editable=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', models.JSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', models.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', models.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
                ('main', models.BooleanField(blank=True, db_column='Main', null=True)),
                ('params', models.JSONField(blank=True, db_column='Params', null=True)),
                ('class_params', models.JSONField(blank=True, db_column='ClassParams', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('calculation_rules', models.ForeignKey(blank=True, db_column='CalculationRulesUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='calculation.CalculationRules')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_created', models.ForeignKey(blank=True, db_column='UserCreatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, db_column='UserUpdatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical calculation rules details',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCalculationRules',
            fields=[
                ('id', models.UUIDField(db_column='UUID', db_index=True, default=None, editable=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', models.JSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', models.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', models.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', models.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', models.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('calculation_class_name', models.CharField(blank=True, db_column='CalculationsClassName', max_length=255, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True)),
                ('priority', models.IntegerField(blank=True, db_column='Priority', null=True)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_created', models.ForeignKey(blank=True, db_column='UserCreatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, db_column='UserUpdatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical calculation rules',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='CalculationRulesDetails',
            fields=[
                ('id', models.UUIDField(db_column='UUID', default=None, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', models.JSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', models.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', models.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
                ('main', models.BooleanField(blank=True, db_column='Main', null=True)),
                ('params', models.JSONField(blank=True, db_column='Params', null=True)),
                ('class_params', models.JSONField(blank=True, db_column='ClassParams', null=True)),
                ('calculation_rules', models.ForeignKey(db_column='CalculationRulesUUID', on_delete=django.db.models.deletion.DO_NOTHING, to='calculation.CalculationRules')),
                ('user_created', models.ForeignKey(db_column='UserCreatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='calculationrulesdetails_user_created', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(db_column='UserUpdatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='calculationrulesdetails_user_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tblCalculationRulesDetails',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
