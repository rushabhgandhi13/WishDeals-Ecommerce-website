# Generated by Django 3.1.4 on 2021-02-15 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210215_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='tilte',
        ),
    ]
