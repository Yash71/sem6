# Generated by Django 3.1.5 on 2021-06-22 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_camera'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=12),
            preserve_default=False,
        ),
    ]
