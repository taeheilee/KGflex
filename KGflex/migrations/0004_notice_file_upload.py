# Generated by Django 3.1 on 2022-08-16 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KGflex', '0003_auto_20220816_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='KGflex/data/%Y/%m/%d/'),
        ),
    ]