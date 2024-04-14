# Generated by Django 5.0.4 on 2024-04-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='pic',
            field=models.URLField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url1',
            field=models.URLField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url10',
            field=models.URLField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url2',
            field=models.URLField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url3',
            field=models.URLField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url4',
            field=models.URLField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url5',
            field=models.URLField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url6',
            field=models.URLField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url7',
            field=models.URLField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url8',
            field=models.URLField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url9',
            field=models.URLField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]
