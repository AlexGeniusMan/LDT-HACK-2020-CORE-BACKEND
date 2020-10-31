# Generated by Django 3.1.2 on 2020-10-31 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20201031_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='is_visible',
            field=models.BooleanField(default=False, verbose_name='Является видимым'),
        ),
        migrations.AlterField(
            model_name='taskdetail',
            name='is_done',
            field=models.BooleanField(default=False, verbose_name='Является сделанным'),
        ),
    ]