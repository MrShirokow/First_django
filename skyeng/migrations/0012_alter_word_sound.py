# Generated by Django 4.0.5 on 2022-06-16 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skyeng', '0011_word_sound'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='sound',
            field=models.FileField(blank=True, upload_to='sounds/'),
        ),
    ]