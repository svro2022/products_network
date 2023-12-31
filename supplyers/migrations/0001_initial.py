# Generated by Django 4.2.7 on 2023-12-03 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('country', models.CharField(max_length=200, verbose_name='Страна')),
                ('city', models.CharField(max_length=200, verbose_name='Город')),
                ('street', models.CharField(max_length=200, verbose_name='Улица')),
                ('house', models.CharField(max_length=100, verbose_name='Номер дома')),
                ('levels', models.IntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], default=0, verbose_name='Уровень структуры')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Задолженность')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор поставщика')),
                ('product', models.ManyToManyField(to='products.product', verbose_name='Продукт')),
                ('supply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='supplyers.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Уровень поставки',
                'verbose_name_plural': 'Уровни поставки',
            },
        ),
    ]
