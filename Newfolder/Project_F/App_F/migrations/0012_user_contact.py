# Generated by Django 4.0.5 on 2022-06-15 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_F', '0011_remove_user_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.IntegerField(default=True),
        ),
    ]
