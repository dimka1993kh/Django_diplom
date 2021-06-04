# Generated by Django 3.1.2 on 2021-06-04 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='update_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', max_length=300)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('creation_date', models.DateField(auto_now=True)),
                ('update_date', models.DateField(default=None, null=True)),
                ('ID_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.product', verbose_name='Товар')),
                ('ID_review_author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв на товар',
                'verbose_name_plural': 'Отзывы на товары',
                'db_table': 'product_review',
            },
        ),
    ]
