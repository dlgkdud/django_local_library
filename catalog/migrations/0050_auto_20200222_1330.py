# Generated by Django 3.0.2 on 2020-02-22 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0049_auto_20200222_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('o', 'On loan'), ('r', 'Reserved'), ('a', 'Available'), ('m', 'Maintenance')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
