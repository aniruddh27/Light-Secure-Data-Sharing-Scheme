# Generated by Django 2.0.2 on 2019-03-13 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appAdmin', '0016_auto_20190206_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='DUTATransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('pub_key', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=20)),
                ('attributes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appAdmin.register')),
            ],
        ),
    ]
