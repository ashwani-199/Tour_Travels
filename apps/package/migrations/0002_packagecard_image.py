# Generated by Django 4.2.2 on 2023-08-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagecard',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Pakages'),
        ),
    ]