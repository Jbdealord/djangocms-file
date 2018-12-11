# Generated by Django 2.1.2 on 2018-12-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_file', '0010_removed_null_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='show_file_size',
            field=models.BooleanField(blank=True, default=False, help_text='Appends the file size at the end of the name.', verbose_name='Show file size'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='show_file_size',
            field=models.BooleanField(blank=True, default=False, help_text='Appends the file size at the end of the name.', verbose_name='Show file size'),
        ),
    ]