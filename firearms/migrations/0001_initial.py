# Generated by Django 3.2.7 on 2021-09-18 22:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('attachments', '0001_initial'),
        ('ammunition', '0001_initial'),
        ('skins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firearm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision_id', models.PositiveIntegerField(default=0, editable=False)),
                ('request_id', models.CharField(default='', editable=False, max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('HG', 'HandGun'), ('LG', 'LongGun')], max_length=2)),
                ('fire_rate', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='Fire rate has to be greter than 0.')])),
                ('clip_capacity', models.PositiveIntegerField()),
                ('clip_cartridges', models.PositiveIntegerField()),
                ('damage', models.FloatField(default=1.0, validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='Cannot deal less than 0 damage.'), django.core.validators.MaxValueValidator(limit_value=100.0, message='Cannot deal more than 100 damage.')])),
                ('ammunition_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ammunition.ammunition')),
                ('attachments', models.ManyToManyField(blank=True, null=True, to='attachments.Attachment')),
                ('skin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skins.skin')),
            ],
        ),
    ]
