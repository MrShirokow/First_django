# Generated by Django 4.0.5 on 2022-06-11 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skyeng', '0003_category_icon_alter_theme_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='text',
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='level',
            field=models.CharField(blank=True, choices=[('A1', 'Beginner'), ('A2', 'Elementary'), ('B1', 'Intermediate'), ('B2', 'Upper-Intermediate'), ('C1', 'Advanced'), ('C2', 'Proficiency')], max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skyeng.theme')),
            ],
            options={
                'verbose_name': 'Word',
                'verbose_name_plural': 'Words',
            },
        ),
    ]