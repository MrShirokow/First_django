# Generated by Django 4.0.5 on 2022-07-13 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skyeng', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='repeat_words',
            field=models.IntegerField(null=True),
        ),
    ]
