from django.db import models
from datetime import date
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User


from django.urls import reverse



class Access(models.Model):
    name = models.CharField(verbose_name="Тип доступа", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип доступа"
        verbose_name_plural = "Тип доступа"

class Position(models.Model):

    name = models.CharField(verbose_name="Название должности", max_length=50)
    salary = models.FloatField(verbose_name="Оклад", max_length=50)

    def unicode(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'



class Discipline(models.Model):
    name = models.CharField(verbose_name="Название дисциплины", max_length=50)
    description = models.TextField(verbose_name="Описание")

    def unicode(self):
        return self.name

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Имя", max_length=50)
    surname = models.CharField(verbose_name="Фамилия", max_length=50)
    middle_name = models.CharField(verbose_name="Отчество", max_length=50, default='Отсутсвут', null=True, blank=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения", default=0)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True)
    fk_position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Должность")
    fk_accses = models.ForeignKey(Access, on_delete=models.CASCADE, verbose_name="Доступ")
    fk_discipline = models.ManyToManyField('Discipline', verbose_name="Дисциплина")

    def unicode(self):
        return self.user

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'



class Student(models.Model):
    """Студенты"""
    name = models.CharField(verbose_name="Имя", max_length=50)
    surname = models.CharField(verbose_name="Фамилия", max_length=50)
    middle_name = models.CharField(verbose_name="Отчество", max_length=50, default='Отсутсвут', null=True, blank=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения", default=0)
    course = models.IntegerField(verbose_name="Курс", default=0)
    number = models.CharField(verbose_name="Номер билета", max_length=50, null=True)
    group = models.ForeignKey('Group_name', verbose_name="Название группы", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

class Group_name(models.Model):
    """Группы"""
    name = models.TextField(verbose_name="Название группы", max_length=100, unique=True)
    description = models.TextField(verbose_name="Описание", max_length=100,)
    fk_discipline = models.ManyToManyField('Discipline', verbose_name="Дисциплина")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

class Homework(models.Model):
    """Информация"""
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    description = models.TextField(verbose_name="Описание")
    date_of_deliviri = models.DateTimeField(verbose_name="Дата назначения работы")
    appointment_date = models.DateTimeField(verbose_name="Дата сдачи работы")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Домашняя работа"
        verbose_name_plural = "Домашняя работа"


class Homework_check(models.Model):
    """Проверка домашней работы"""
    assessment = models.CharField(verbose_name="Оценка", max_length=1)
    fk_employee = models.ForeignKey(UserProfile, verbose_name="Сотрудник", on_delete=models.PROTECT)
    fk_homework = models.ForeignKey(Homework, verbose_name="Домашняя работа", on_delete=models.PROTECT)
    fk_student = models.ManyToManyField(Student, verbose_name="Студент")

    def __str__(self):
        return self.assessment

    class Meta:
        verbose_name = "Проверка домашней работы"
        verbose_name_plural = "Проверка домашней работы"


class Information(models.Model):
    """Информация"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to="information_shots/", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информация"


class Diary(models.Model):

    def __str__(self):
        return self.fk_student
    fk_student = models.ForeignKey(Student, verbose_name="Студент", on_delete=models.PROTECT)
    fk_discipline = models.ForeignKey(Discipline, verbose_name="Дисциплина", on_delete=models.PROTECT)
    fk_homework_check = models.ForeignKey(Homework_check, verbose_name="Работа", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Дневник"
        verbose_name_plural = "Дневник"
