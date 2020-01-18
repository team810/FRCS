# Generated by Django 3.0.2 on 2020-01-18 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teams.Team')),
            ],
        ),
    ]
