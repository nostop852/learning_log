# Generated by Django 4.1 on 2022-09-16 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bili', '0002_entry_exercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='topic',
            field=models.CharField(default='none', max_length=160),
        ),
    ]
