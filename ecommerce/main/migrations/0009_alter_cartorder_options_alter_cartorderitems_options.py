# Generated by Django 4.1.4 on 2023-03-08 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_cartorder_cartorderitems'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartorder',
            options={'verbose_name_plural': '8. Orders'},
        ),
        migrations.AlterModelOptions(
            name='cartorderitems',
            options={'verbose_name_plural': '9. Order Items'},
        ),
    ]
