# Generated by Django 4.2.2 on 2023-07-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0006_alter_resume_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
