# Generated by Django 3.1 on 2022-08-19 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KGflex', '0014_auto_20220819_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='umovie',
            name='content1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='umovie',
            name='content2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='umovie',
            name='content3',
            field=models.TextField(),
        ),
    ]
