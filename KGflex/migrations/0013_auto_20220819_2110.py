# Generated by Django 3.1 on 2022-08-19 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KGflex', '0012_auto_20220819_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='entertainment',
            name='content1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='entertainment',
            name='content2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='entertainment',
            name='content3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='entertainment',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='kmovie',
            name='content1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='kmovie',
            name='content2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='kmovie',
            name='content3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='kmovie',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='umovie',
            name='content1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='umovie',
            name='content2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='umovie',
            name='content3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='umovie',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]