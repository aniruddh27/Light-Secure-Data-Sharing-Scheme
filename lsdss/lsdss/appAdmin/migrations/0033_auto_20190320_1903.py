# Generated by Django 2.1.7 on 2019-03-20 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appAdmin', '0032_auto_20190320_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dotatransaction',
            old_name='pub_key',
            new_name='_pub_key',
        ),
    ]