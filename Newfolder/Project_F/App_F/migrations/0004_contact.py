# Generated by Django 4.0.5 on 2022-06-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_F', '0003_rename_address_user_city_alter_user_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('city', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
    ]
