# Generated by Django 4.0.3 on 2022-05-08 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srbase', '0010_remove_department_reposiotry_department_repository'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='repository',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='srbase.repository'),
        ),
    ]
