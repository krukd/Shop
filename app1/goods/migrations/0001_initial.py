# Generated by Django 4.2.15 on 2024-08-12 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]
