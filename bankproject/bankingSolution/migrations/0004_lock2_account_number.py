# Generated by Django 4.0.6 on 2022-10-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingSolution', '0003_sendmoney_holder_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='lock2',
            name='account_number',
            field=models.CharField(default='', max_length=122),
        ),
    ]
