# Generated by Django 4.1.7 on 2023-03-09 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_alter_individualentrepreneur_debt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualentrepreneur',
            name='debt',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
