# Generated by Django 2.0.2 on 2019-01-22 23:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appAdmin', '0012_ownerfileupload_file_upload_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerfileupload',
            name='file_status',
            field=models.CharField(default=datetime.datetime(2019, 1, 22, 23, 32, 36, 314717, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
