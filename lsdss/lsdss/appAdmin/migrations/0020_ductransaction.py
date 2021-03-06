# Generated by Django 2.0.2 on 2019-03-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAdmin', '0019_dodutransaction_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='DUCTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('attributes', models.CharField(max_length=500)),
                ('pub_key', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=20)),
                ('file_name', models.CharField(max_length=30)),
                ('enc_file', models.URLField()),
            ],
        ),
    ]
