# Generated by Django 4.0.5 on 2022-06-15 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_F', '0008_rename_contact_us_contact_alter_contact_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Enquiry',
        ),
        migrations.AlterModelTable(
            name='enquiry',
            table='Enquiry',
        ),
    ]
