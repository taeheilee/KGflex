# Generated by Django 3.1 on 2022-08-19 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KGflex', '0011_auto_20220819_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='kdrama',
            name='content1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='kdrama',
            name='content2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='kdrama',
            name='content3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='kdrama',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
