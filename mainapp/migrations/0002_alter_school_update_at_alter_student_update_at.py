# Generated by Django 4.0.6 on 2023-06-24 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='Update_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Update_at',
            field=models.DateTimeField(null=True),
        ),
    ]
