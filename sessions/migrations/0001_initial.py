# Generated by Django 3.2.7 on 2021-09-18 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision_id', models.PositiveIntegerField(default=0, editable=False)),
                ('request_id', models.CharField(default='', editable=False, max_length=100)),
                ('number_of_teams', models.PositiveIntegerField()),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maps.map')),
                ('players', models.ManyToManyField(blank=True, null=True, to='players.Player')),
            ],
        ),
    ]
