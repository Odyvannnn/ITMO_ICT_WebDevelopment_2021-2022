# Generated by Django 3.2.9 on 2021-12-03 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels_app', '0007_review_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hotels_app.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hotels_app.hotel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='reservation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hotels_app.reservation'),
            preserve_default=False,
        ),
    ]
