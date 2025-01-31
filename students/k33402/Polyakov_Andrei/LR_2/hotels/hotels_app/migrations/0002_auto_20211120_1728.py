# Generated by Django 3.2.9 on 2021-11-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='approval',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
    ]
