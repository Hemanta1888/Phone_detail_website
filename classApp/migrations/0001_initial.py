# Generated by Django 3.2.5 on 2021-12-30 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pname', models.CharField(max_length=100)),
                ('Porigin', models.CharField(max_length=100)),
                ('Pyear', models.IntegerField()),
                ('Pabout', models.TextField()),
            ],
        ),
    ]