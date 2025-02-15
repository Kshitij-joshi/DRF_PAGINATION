# Generated by Django 3.2.15 on 2025-02-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_moviedata_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('average_rating', models.FloatField()),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
    ]
