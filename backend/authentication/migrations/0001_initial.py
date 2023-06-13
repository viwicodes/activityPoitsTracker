# Generated by Django 4.2.2 on 2023-06-13 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('ph', models.CharField(max_length=12)),
                ('sem', models.CharField(max_length=2)),
                ('points', models.IntegerField(default=0)),
                ('role', models.CharField(default='', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('ph', models.CharField(max_length=12)),
                ('sem', models.CharField(max_length=2)),
                ('points', models.IntegerField(default=0)),
                ('role', models.CharField(default='', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
