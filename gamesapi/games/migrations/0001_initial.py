# Generated by Django 3.1 on 2020-08-13 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('release_date', models.DateTimeField()),
                ('game_category', models.CharField(blank=True, default='', max_length=200)),
                ('played', models.BooleanField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
