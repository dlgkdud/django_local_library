# Generated by Django 3.0.2 on 2020-02-23 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0055_auto_20200223_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('a', 'Available'), ('o', 'On loan'), ('r', 'Reserved')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
