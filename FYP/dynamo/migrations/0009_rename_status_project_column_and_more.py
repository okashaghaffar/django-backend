# Generated by Django 5.0.3 on 2024-04-27 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamo', '0008_project_price_alter_project_start'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='status',
            new_name='column',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='end',
            new_name='deadline',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='project',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 13, 7, 56, 228005)),
        ),
    ]