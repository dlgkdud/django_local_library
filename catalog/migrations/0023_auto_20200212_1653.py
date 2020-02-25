# Generated by Django 3.0.2 on 2020-02-12 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_auto_20200212_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('r', 'Reserved'), ('m', 'Maintenance'), ('a', 'Available'), ('o', 'On loan')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
