# Generated by Django 5.0.2 on 2024-02-22 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('location', models.IntegerField()),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
