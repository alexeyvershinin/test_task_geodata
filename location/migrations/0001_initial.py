# Generated by Django 4.1.6 on 2023-02-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlotData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200, null=True)),
                ('center_point_x', models.FloatField(null=True)),
                ('center_point_y', models.FloatField(null=True)),
            ],
        ),
    ]
