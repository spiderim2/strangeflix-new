# Generated by Django 3.1.2 on 2020-10-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20201021_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist_video',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
