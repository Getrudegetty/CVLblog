# Generated by Django 4.0.3 on 2022-03-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_web'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=200, verbose_name='Last Name')),
                ('phone', models.IntegerField(verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('message', models.TextField(blank=True, verbose_name='message')),
            ],
            options={
                'verbose_name': 'Contact Profile',
                'verbose_name_plural': 'Contact Profiles',
            },
        ),
        migrations.DeleteModel(
            name='Web',
        ),
    ]
