# Generated by Django 3.2.3 on 2021-05-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210524_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appearence',
            name='footer_credit',
            field=models.TextField(default='Copyright ©2021 All rights reserved | Developed  by Django Team', max_length=160),
        ),
    ]