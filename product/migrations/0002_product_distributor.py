# Generated by Django 4.2.7 on 2023-12-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='distributor',
            field=models.CharField(default='Null', max_length=200),
        ),
    ]
