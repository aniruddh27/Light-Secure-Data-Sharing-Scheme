# Generated by Django 2.0.2 on 2019-01-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAdmin', '0006_ownerfileupload_owner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerfileupload',
            name='owner_file',
            field=models.FileField(upload_to='media'),
        ),
    ]
