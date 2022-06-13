# Generated by Django 4.0.3 on 2022-05-09 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srbase', '0013_title_college_title_alter_repository_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='department',
        ),
        migrations.AddField(
            model_name='department',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='srbase.college'),
        ),
    ]
