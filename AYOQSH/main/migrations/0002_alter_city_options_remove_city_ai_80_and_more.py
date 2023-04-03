# Generated by Django 4.1.7 on 2023-04-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'City'},
        ),
        migrations.RemoveField(
            model_name='city',
            name='ai_80',
        ),
        migrations.RemoveField(
            model_name='city',
            name='ai_90',
        ),
        migrations.RemoveField(
            model_name='city',
            name='ai_91',
        ),
        migrations.RemoveField(
            model_name='city',
            name='ai_92',
        ),
        migrations.RemoveField(
            model_name='city',
            name='ai_98',
        ),
        migrations.AddField(
            model_name='city',
            name='fuel',
            field=models.CharField(default='', max_length=50, verbose_name='ai_98'),
        ),
    ]
