# Generated by Django 3.1.7 on 2021-05-10 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='forget_password_token',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
