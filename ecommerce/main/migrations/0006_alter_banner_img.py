# Generated by Django 3.2.16 on 2023-01-05 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20230105_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(upload_to='brand_imgs/'),
        ),
    ]
