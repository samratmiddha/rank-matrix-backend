# Generated by Django 3.2.7 on 2023-02-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rank_matrix', '0003_auto_20230222_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='available_categories',
            field=models.ManyToManyField(blank=True, default=None, related_name='Available_Categories', to='rank_matrix.Category'),
        ),
    ]
