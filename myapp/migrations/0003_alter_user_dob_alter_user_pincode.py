# Generated by Django 4.0.4 on 2022-05-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
    ]
