# Generated by Django 2.2.2 on 2019-06-21 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20190621_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='department',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]