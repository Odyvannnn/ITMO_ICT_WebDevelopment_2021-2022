# Generated by Django 3.2.9 on 2021-11-20 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels_app', '0002_auto_20211120_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='approval',
            field=models.CharField(choices=[('Заселен', 'Заселен'), ('Не заселен', 'Не заселен')], max_length=10),
        ),
    ]
