# Generated by Django 2.0.6 on 2018-08-07 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_auto_20180807_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='gross_salary',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='应发工资'),
        ),
    ]