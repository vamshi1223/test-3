# Generated by Django 5.0.7 on 2024-08-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educationapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phonenumber', models.CharField()),
                ('typeyourmessage', models.CharField(max_length=200)),
            ],
        ),
    ]