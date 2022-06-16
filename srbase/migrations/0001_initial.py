# Generated by Django 4.0.4 on 2022-06-14 17:44

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
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Some String', max_length=255)),
                ('docfile', models.FileField(default='DEFAULT VALUE', null=True, upload_to='document/%d/%m/%Y')),
                ('description', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('authors', models.ManyToManyField(blank=True, related_name='authors', to=settings.AUTH_USER_MODEL)),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='srbase.college')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
