# Generated by Django 3.2.9 on 2021-12-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artstore', '0003_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
