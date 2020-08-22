# Generated by Django 3.1 on 2020-08-22 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.DateTimeField(blank=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
