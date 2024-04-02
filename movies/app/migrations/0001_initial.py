# Generated by Django 5.0.2 on 2024-03-05 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('year', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='movies')),
            ],
        ),
    ]
