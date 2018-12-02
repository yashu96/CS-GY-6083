# Generated by Django 2.0.5 on 2018-05-09 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_auto_20180507_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='city',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='image',
            name='street_address',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='zipcode',
            field=models.CharField(max_length=5),
        ),
    ]
