# Generated by Django 4.1.3 on 2022-11-30 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('located', models.CharField(choices=[('Dry', 'Dry'), ('Frozen', 'Frozen'), ('Walkin', 'Walkin'), ('Lowboy', 'Lowboy')], max_length=6)),
                ('flag', models.CharField(blank=True, choices=[('Low', 'Low'), ('Out', 'Out'), ('Dead', 'Dead'), ('Expiring', 'Expiring')], max_length=8)),
                ('to_whiteboard', models.BooleanField(null=True)),
                ('name', models.CharField(max_length=200)),
                ('par', models.CharField(max_length=200)),
                ('on_hand', models.CharField(blank=True, max_length=200)),
                ('need', models.CharField(blank=True, max_length=200)),
                ('exp_date', models.CharField(blank=True, max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=69)),
                ('body', models.TextField(max_length=666)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Prep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, choices=[('Appetizers', 'Appetizers'), ('Entrees', 'Entrees'), ('Sides', 'Sides'), ('Desserts', 'Desserts')], max_length=10)),
                ('flag', models.CharField(blank=True, choices=[('Low', 'Low'), ('Out', 'Out'), ('Dead', 'Dead'), ('Expiring', 'Expiring')], max_length=8)),
                ('to_whiteboard', models.BooleanField(null=True)),
                ('name', models.CharField(max_length=200)),
                ('par', models.CharField(max_length=200)),
                ('on_hand', models.CharField(blank=True, max_length=200)),
                ('need', models.CharField(blank=True, max_length=200)),
                ('exp_date', models.CharField(blank=True, max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('in_use', models.BooleanField()),
                ('component_of', models.TextField()),
                ('details', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(choices=[('Appetizers', 'Appetizers'), ('Entrees', 'Entrees'), ('Sides', 'Sides'), ('Desserts', 'Desserts')], max_length=10)),
                ('dish', models.CharField(max_length=200)),
                ('prep_tasks', models.TextField(blank=True)),
                ('ingredients', models.TextField()),
                ('directions', models.TextField()),
                ('prep_time', models.CharField(max_length=200)),
                ('cooking_time', models.CharField(max_length=200)),
                ('batch_size', models.CharField(max_length=200)),
                ('par', models.CharField(blank=True, max_length=200)),
                ('shelf_life', models.CharField(blank=True, max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('in_use', models.BooleanField()),
                ('component_of', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(choices=[('Opening', 'Opening'), ('Closing', 'Closing'), ('Mid', 'Mid')], max_length=7)),
                ('name', models.CharField(max_length=200)),
                ('checked', models.BooleanField(null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('NEW', 'NEW'), ('OUT', 'OUT'), ('GONE', 'GONE'), ('CHANGE', 'CHANGE')], max_length=6)),
                ('subject', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
