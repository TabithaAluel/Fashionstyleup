# Generated by Django 3.2.9 on 2021-11-17 20:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0008_auto_20211116_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pair_with',
            field=models.ManyToManyField(blank=True, related_name='pair_with', to=settings.AUTH_USER_MODEL),
        ),
    ]
