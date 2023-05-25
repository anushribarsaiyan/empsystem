# Generated by Django 4.2 on 2023-04-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('emp_image', models.ImageField(upload_to='empimg')),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('hire_date', models.DateField()),
            ],
        ),
    ]
