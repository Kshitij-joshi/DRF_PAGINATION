# Generated by Django 3.2.15 on 2025-02-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moviedata',
            options={'verbose_name': 'Movie Data', 'verbose_name_plural': 'Movie Data'},
        ),
        migrations.AddField(
            model_name='moviedata',
            name='category',
            field=models.CharField(default='family', max_length=200),
        ),
    ]
