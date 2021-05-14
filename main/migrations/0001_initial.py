# Generated by Django 3.2 on 2021-05-14 18:32

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
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тип доступа')),
            ],
            options={
                'verbose_name': 'Тип доступа',
                'verbose_name_plural': 'Тип доступа',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название дисциплины')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'verbose_name_plural': 'Дисциплины',
            },
        ),
        migrations.CreateModel(
            name='Group_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, unique=True, verbose_name='Название группы')),
                ('description', models.TextField(max_length=100, verbose_name='Описание')),
                ('course', models.IntegerField(default=0, verbose_name='Курс')),
                ('fk_discipline', models.ManyToManyField(to='main.Discipline', verbose_name='Дисциплина')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('date_of_deliviri', models.DateTimeField(verbose_name='Дата назначения работы')),
                ('appointment_date', models.DateTimeField(verbose_name='Дата сдачи работы')),
                ('fk_group', models.ManyToManyField(to='main.Group_name', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Домашняя работа',
                'verbose_name_plural': 'Домашняя работа',
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Информация',
                'verbose_name_plural': 'Информация',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название должности')),
                ('salary', models.FloatField(max_length=50, verbose_name='Оклад')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, default='Отсутсвут', max_length=50, null=True, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(default=0, verbose_name='Дата рождения')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('fk_accses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.access', verbose_name='Доступ')),
                ('fk_position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.position', verbose_name='Должность')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, default='Отсутсвут', max_length=50, null=True, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(default=0, verbose_name='Дата рождения')),
                ('number', models.CharField(max_length=50, null=True, verbose_name='Номер билета')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.group_name', verbose_name='Название группы')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='Homework_check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment', models.CharField(max_length=1, verbose_name='Оценка')),
                ('fk_employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
                ('fk_homework', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.homework', verbose_name='Домашняя работа')),
                ('fk_student', models.ManyToManyField(to='main.Student', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Проверка домашней работы',
                'verbose_name_plural': 'Проверка домашней работы',
            },
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_discipline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.discipline', verbose_name='Дисциплина')),
                ('fk_employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Преподаватель')),
                ('fk_group_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.group_name', verbose_name='Группы')),
            ],
            options={
                'verbose_name': 'Распределение',
                'verbose_name_plural': 'Распределения',
            },
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_discipline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.discipline', verbose_name='Дисциплина')),
                ('fk_homework_check', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.homework_check', verbose_name='Работа')),
                ('fk_student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.student', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Дневник',
                'verbose_name_plural': 'Дневник',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_visit', models.DateTimeField(verbose_name='Дата проведения занятия')),
                ('presence', models.CharField(choices=[('Присутствует', 'Присутствует'), ('Отсутствует', 'Отсутствует')], max_length=12, verbose_name='Присутсвие на занятии')),
                ('fk_discipline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.discipline', verbose_name='Дисциплина')),
                ('fk_student', models.ManyToManyField(to='main.Student', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Посещаемость',
                'verbose_name_plural': 'Посещаемость',
            },
        ),
    ]
