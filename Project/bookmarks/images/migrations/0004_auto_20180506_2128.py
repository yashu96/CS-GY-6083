# Generated by Django 2.0.5 on 2018-05-06 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_remove_image_total_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
        migrations.AddField(
            model_name='image',
            name='amenities',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='city',
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AddField(
            model_name='image',
            name='listing_type',
            field=models.CharField(choices=[('Rent', 'Rent'), ('Sell', 'Sell'), ('Buy', 'Buy')], default='Rent', max_length=4),
        ),
        migrations.AddField(
            model_name='image',
            name='price',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='street_address',
            field=models.CharField(blank=True, db_index=True, max_length=200),
        ),
        migrations.AddField(
            model_name='image',
            name='zipcode',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d'),
        ),
    ]
