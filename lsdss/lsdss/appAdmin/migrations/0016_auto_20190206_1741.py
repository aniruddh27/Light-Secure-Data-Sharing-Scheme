# Generated by Django 2.0.2 on 2019-02-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAdmin', '0015_cloudtransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='module',
            field=models.CharField(choices=[('Owner', 'Owner'), ('User', 'User'), ('tpa', 'tpa'), ('admin', 'admin'), ('espdsp', 'espdsp'), ('cloud', 'cloud')], max_length=20),
        ),
    ]
