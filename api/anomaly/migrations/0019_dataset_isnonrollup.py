# Generated by Django 3.2.5 on 2021-10-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anomaly', '0018_rootcauseanalysis_taskids'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='isNonRollup',
            field=models.BooleanField(default=False),
        ),
    ]