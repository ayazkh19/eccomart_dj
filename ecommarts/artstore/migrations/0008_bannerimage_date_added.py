# Generated by Django 3.2.9 on 2021-12-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artstore', '0007_bannerimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerimage',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
