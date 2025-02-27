# Generated by Django 5.1.4 on 2024-12-20 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('task_description', models.CharField(max_length=1000)),
                ('task_date', models.DateTimeField(auto_now_add=True)),
                ('task_check', models.BooleanField(default=False)),
            ],
        ),
    ]
