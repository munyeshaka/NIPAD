# Generated by Django 4.0 on 2021-12-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nipadapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
