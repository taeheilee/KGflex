# Generated by Django 3.1 on 2022-08-19 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KGflex', '0018_auto_20220819_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kdrama',
            name='content1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='kdrama',
            name='content2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='kdrama',
            name='content3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='umovie',
            name='content1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='umovie',
            name='content2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='umovie',
            name='content3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
