# Generated by Django 4.0.5 on 2022-06-12 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_F', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.IntegerField(null=True),
        ),
    ]