# Generated by Django 2.1.1 on 2018-10-19 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0004_auto_20181009_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='profile_img')),
            ],
        ),
    ]