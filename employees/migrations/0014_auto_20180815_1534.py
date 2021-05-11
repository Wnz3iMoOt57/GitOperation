# Generated by Django 2.0.6 on 2018-08-15 07:34

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0013_auto_20180813_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreport',
            name='assess',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='评价内容'),
        ),
        migrations.AlterField(
            model_name='dailyreport',
            name='report_content',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='日报内容'),
        ),
    ]