# Generated by Django 2.2 on 2019-05-31 00:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_inspection'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='province',
            field=models.CharField(default='BC', max_length=2),
        ),
        migrations.AddField(
            model_name='operator',
            name='operationName',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
        migrations.AddField(
            model_name='operator',
            name='operator_type',
            field=models.CharField(choices=[('BREEDER', 'breeder'), ('SELLER', 'seller'), ('BREEDER & SELLER', 'breeder & seller')], default='BREEDER', max_length=20),
        ),
        migrations.AddField(
            model_name='operator',
            name='type',
            field=models.CharField(choices=[('Email', 'email'), ('Mail', 'mail')], default='Email', max_length=10),
        ),
        migrations.CreateModel(
            name='Risk_Factor_MetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accidental_breeding', models.BooleanField(default=False)),
                ('num_workers', models.IntegerField()),
                ('opn_URL', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('num_breeds_dogs', models.IntegerField()),
                ('num_breeds_cats', models.IntegerField()),
                ('has_vet', models.BooleanField(default=False)),
                ('has_perm_id', models.BooleanField(default=False)),
                ('perm_id_type', models.CharField(choices=[('TATTOO', 'tattoo'), ('MICROCHIP', 'microchip'), ('OTHER', 'other')], default='TATTOO', max_length=10)),
                ('perm_id_other', models.CharField(blank=True, default='', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='riskmetadata', to='api.Operator')),
            ],
            options={
                'verbose_name_plural': 'RiskFactorsMeta',
            },
        ),
        migrations.CreateModel(
            name='Risk_Factor_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_dogs_intact', models.IntegerField(default=0)),
                ('num_litter_whelped', models.IntegerField(default=0)),
                ('num_cats_intact', models.IntegerField(default=0)),
                ('num_litter_queened', models.IntegerField(default=0)),
                ('num_sold', models.IntegerField(default=0)),
                ('num_transferred', models.IntegerField(default=0)),
                ('num_traded', models.IntegerField(default=0)),
                ('num_leased', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_data', to='api.Operator')),
            ],
            options={
                'verbose_name_plural': 'RiskFactorsData',
            },
        ),
        migrations.CreateModel(
            name='Association_Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assocName', models.CharField(blank=True, default='', max_length=50)),
                ('membershipNum', models.CharField(blank=True, default='', max_length=10)),
                ('assoc_URL', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='associations', to='api.Operator')),
            ],
            options={
                'verbose_name_plural': 'Associations',
            },
        ),
    ]