# Generated by Django 2.1.7 on 2019-02-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutshop',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
