# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 20:44
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='_JournalEntryDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('amount_debit', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=30, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Debit')),
                ('amount_credit', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=30, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Credit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('code', models.CharField(max_length=255, verbose_name='Code')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('mandatory', models.BooleanField(default=False, verbose_name='Is Mandatory')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='accounting.Account', verbose_name='Parent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('generator_object_id', models.PositiveIntegerField(null=True)),
                ('creation', models.CharField(max_length=1, verbose_name='Creation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JournalEntryOpenStatement',
            fields=[
                ('journalentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounting.JournalEntry')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='open_statement', to='accounting.Account', verbose_name='Account')),
            ],
            options={
                'abstract': False,
            },
            bases=('accounting.journalentry',),
        ),
        migrations.AddField(
            model_name='journalentry',
            name='generator_content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='_journalentrydetail',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Account', verbose_name='Account'),
        ),
        migrations.AddField(
            model_name='_journalentrydetail',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.JournalEntry', verbose_name='Entry'),
        ),
    ]
