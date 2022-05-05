# Generated by Django 4.0.4 on 2022-05-05 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sciekipolskie', '0003_remove_listofworkers_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeTaskDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=15)),
                ('category', models.CharField(max_length=30)),
                ('deadline', models.DateField()),
                ('done_btn', models.BooleanField(default=False)),
            ],
        ),
    ]
