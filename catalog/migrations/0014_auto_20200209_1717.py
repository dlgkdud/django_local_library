# Generated by Django 3.0.2 on 2020-02-09 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20200209_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Available'), ('o', 'On loan'), ('m', 'Maintenance'), ('r', 'Reserved')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
