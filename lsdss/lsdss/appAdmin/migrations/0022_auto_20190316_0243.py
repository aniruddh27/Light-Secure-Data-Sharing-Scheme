# Generated by Django 2.0.2 on 2019-03-15 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAdmin', '0021_ductransaction_owner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ductransaction',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]
