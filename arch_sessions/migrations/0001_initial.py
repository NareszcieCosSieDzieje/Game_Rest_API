# Generated by Django 3.2.7 on 2021-09-18 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialized_map', models.TextField()),
                ('serialized_players', models.TextField()),
            ],
        ),
    ]
