# Generated by Django 5.0.4 on 2024-04-24 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_student_options_alter_student_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=20, unique=True)),
                ('course_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('instructor_name', models.CharField(max_length=100)),
                ('prerequisites', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]
