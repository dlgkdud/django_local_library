# Generated by Django 3.0.2 on 2020-02-22 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0052_auto_20200222_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('r', 'Reserved'), ('a', 'Available'), ('m', 'Maintenance'), ('o', 'On loan')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
