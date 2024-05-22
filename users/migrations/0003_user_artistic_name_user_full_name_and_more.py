# Generated by Django 5.0 on 2024-01-04 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_artistic_name_remove_user_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='artistic_name',
            field=models.CharField(default='Junio', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
