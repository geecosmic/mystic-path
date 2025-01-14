# Generated by Django 5.1.2 on 2025-01-05 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('message_for', models.TextField(null=True)),
                ('message_against', models.TextField(null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='YearlyPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('message_for', models.TextField(null=True)),
                ('message_against', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
