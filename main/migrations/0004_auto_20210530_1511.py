# Generated by Django 3.1.2 on 2021-05-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='update_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
