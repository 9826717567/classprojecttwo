# Generated by Django 4.0.5 on 2022-06-15 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_F', '0010_delete_enquiry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contact',
        ),
    ]