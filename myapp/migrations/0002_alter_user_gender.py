# Generated by Django 4.0.4 on 2022-05-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'not specified')], default=0),
        ),
    ]
