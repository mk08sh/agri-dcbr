# Generated by Django 2.2.1 on 2019-05-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operator',
            old_name='numCats',
            new_name='aptNum',
        ),
        migrations.RenameField(
            model_name='operator',
            old_name='numDogs',
            new_name='regNum',
        ),
        migrations.RemoveField(
            model_name='operator',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='operator',
            name='name',
        ),
        migrations.AddField(
            model_name='operator',
            name='city',
            field=models.CharField(default='Victoria', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operator',
            name='email',
            field=models.CharField(default='a@b.com', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operator',
            name='firstName',
            field=models.CharField(default='John', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operator',
            name='lastName',
            field=models.CharField(default='Smith', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operator',
            name='middleName',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operator',
            name='phoneNum',
            field=models.CharField(default='250-555-1212', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operator',
            name='postalCode',
            field=models.CharField(default='V1V 1V1', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operator',
            name='province',
            field=models.CharField(default='BC', max_length=2),
        ),
        migrations.AddField(
            model_name='operator',
            name='streetName',
            field=models.CharField(default='Douglas', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operator',
            name='streetNum',
            field=models.CharField(default='123', max_length=50),
            preserve_default=False,
        ),
    ]
