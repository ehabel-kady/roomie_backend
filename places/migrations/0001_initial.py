# Generated by Django 3.0.2 on 2020-01-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(default='', max_length=150, null=True)),
                ('latitude', models.DecimalField(decimal_places=9, max_digits=9)),
                ('longtude', models.DecimalField(decimal_places=9, max_digits=9)),
                ('photo_1', models.ImageField(null=True, upload_to='uploads/')),
                ('photo_2', models.ImageField(null=True, upload_to='uploads/')),
                ('photo_3', models.ImageField(null=True, upload_to='uploads/')),
                ('photo_4', models.ImageField(null=True, upload_to='uploads/')),
                ('photo_5', models.ImageField(null=True, upload_to='uploads/')),
                ('phone_number', models.CharField(default='', max_length=100, null=True)),
                ('price', models.IntegerField()),
                ('ameneties_1', models.CharField(default='', max_length=100, null=True)),
                ('ameneties_2', models.CharField(default='', max_length=100, null=True)),
                ('ameneties_3', models.CharField(default='', max_length=100, null=True)),
                ('ameneties_4', models.CharField(default='', max_length=100, null=True)),
                ('ameneties_5', models.CharField(default='', max_length=100, null=True)),
                ('ameneties_6', models.CharField(default='', max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Offer',
                'verbose_name_plural': 'Offers',
            },
        ),
    ]
