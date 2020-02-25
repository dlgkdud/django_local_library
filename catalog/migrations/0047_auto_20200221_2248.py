# Generated by Django 3.0.2 on 2020-02-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0046_auto_20200221_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('a', 'Available'), ('r', 'Reserved'), ('o', 'On loan')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
