# Generated by Django 3.1 on 2022-08-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KGflex', '0015_auto_20220819_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kdrama',
            name='content1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='kdrama',
            name='content2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='kdrama',
            name='content3',
            field=models.TextField(),
        ),
    ]