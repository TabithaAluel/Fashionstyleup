# Generated by Django 3.2.9 on 2021-11-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0005_wishitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='wishitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]