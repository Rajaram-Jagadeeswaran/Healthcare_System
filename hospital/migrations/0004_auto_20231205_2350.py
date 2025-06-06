# Generated by Django 2.1.15 on 2023-12-05 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_auto_20231026_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthrecord',
            name='patient',
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='blood_sugar_level',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='healthrecord',
            name='body_temperature',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='healthrecord',
            name='cholesterol',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='healthrecord',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='healthrecord',
            name='respiratory_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthrecord',
            name='weight',
            field=models.FloatField(),
        ),
    ]
