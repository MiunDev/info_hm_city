# Generated by Django 3.1.7 on 2021-03-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picnic_area_app', '0010_auto_20210311_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picnicarea',
            name='DATE_UPDATE',
            field=models.DateTimeField(blank=True, default='2021-03-11 12:10'),
        ),
        migrations.AlterField(
            model_name='picnicarea',
            name='THE_PHOTO',
            field=models.ImageField(null=True, upload_to='picnic_area/', verbose_name='Фото'),
        ),
    ]
