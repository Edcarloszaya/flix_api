# Generated by Django 5.1.3 on 2024-12-05 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='nationality',
            field=models.CharField(blank=True, choices=[('USA', 'Estados Unidos'), ('BRAZIL', 'Brasil')], max_length=100, null=True),
        ),
    ]
