# Generated by Django 2.0.13 on 2019-06-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190617_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, default=False, null=True, upload_to=''),
        ),
    ]
