# Generated by Django 3.1.4 on 2021-02-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210215_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='tilte',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]