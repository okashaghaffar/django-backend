# Generated by Django 5.0.3 on 2024-04-27 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamo', '0009_rename_status_project_column_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 23, 50, 42, 346767)),
        ),
    ]
