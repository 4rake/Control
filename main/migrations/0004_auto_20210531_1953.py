# Generated by Django 3.2 on 2021-05-31 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_remove_homework_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='fk_employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.userprofile', verbose_name='Преподаватель'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
