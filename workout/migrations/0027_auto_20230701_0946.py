# Generated by Django 3.2.19 on 2023-07-01 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0026_alter_workout_number_of_exercises'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='workout_done',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='workout_start',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
