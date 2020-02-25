# Generated by Django 3.0.2 on 2020-02-16 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_auto_20200216_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('o', 'On loan'), ('a', 'Available'), ('m', 'Maintenance'), ('r', 'Reserved')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
