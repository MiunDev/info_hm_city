# Generated by Django 3.1.7 on 2021-03-11 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picnic_area_app', '0007_auto_20210301_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AlterField(
            model_name='picnicarea',
            name='DATE_UPDATE',
            field=models.DateTimeField(blank=True, default='2021-03-11 09:44'),
        ),
        migrations.AddField(
            model_name='picnicarea',
            name='CATEGORY',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='picnic_area_app.category', verbose_name='Категория'),
        ),
    ]
