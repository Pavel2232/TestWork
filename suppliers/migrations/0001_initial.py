# Generated by Django 4.1.7 on 2023-03-09 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('contry', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('house', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('model_product', models.CharField(max_length=200)),
                ('date_start_sale', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('debt', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.contact')),
                ('product', models.ManyToManyField(to='suppliers.product')),
            ],
            options={
                'verbose_name': 'Завод',
                'verbose_name_plural': 'Заводы',
            },
        ),
        migrations.CreateModel(
            name='RetailNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('debt', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.contact')),
                ('product', models.ManyToManyField(to='suppliers.product')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.suppliers')),
            ],
            options={
                'verbose_name': 'Розничная сеть',
                'verbose_name_plural': 'Розничные сети',
            },
        ),
        migrations.CreateModel(
            name='IndividualEntrepreneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('debt', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.contact')),
                ('product', models.ManyToManyField(to='suppliers.product')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.retailnetwork')),
            ],
            options={
                'verbose_name': 'Индивидульный пердприниматель',
                'verbose_name_plural': 'Индивидульные предприниматели',
            },
        ),
    ]