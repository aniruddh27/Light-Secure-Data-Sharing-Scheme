# Generated by Django 2.1.7 on 2019-03-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAdmin', '0035_auto_20190320_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dotatransaction',
            name='pub_key',
            field=models.BinaryField(),
        ),
    ]
