# Generated by Django 4.0.5 on 2022-06-15 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_F', '0004_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact',
            new_name='phone',
        ),
    ]
