# Generated by Django 4.1.3 on 2023-02-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('value', models.FloatField()),
                ('description', models.TextField()),
                ('ratirng', models.FloatField()),
            ],
        ),
    ]