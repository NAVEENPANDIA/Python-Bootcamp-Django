# Generated by Django 4.0.4 on 2022-06-07 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_booking_booking_number_alter_user_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]