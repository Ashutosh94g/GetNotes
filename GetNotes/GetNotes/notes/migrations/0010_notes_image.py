# Generated by Django 2.2.2 on 2019-07-21 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_auto_20190621_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]