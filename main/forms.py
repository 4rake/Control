from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.contrib.admin import widgets

from snowpenguin.django.recaptcha3.fields import ReCaptchaField

class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    captcha = ReCaptchaField()

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'surname', 'middle_name', 'date_of_birth', 'number', 'group',)
        widgets = {
            'date_of_birth': DateInput,
        }

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'name', 'surname', 'middle_name', 'date_of_birth', 'description', 'image', 'fk_position', 'fk_accses',)
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': DateInput,
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'}),
            'fk_position': forms.Select(attrs={'class': 'form-control'}),
            'fk_accses': forms.Select(attrs={'class': 'form-control'}),
            'fk_discipline': forms.Select(attrs={'class': 'form-control'}),

        }
class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ('name', 'salary',)



class Grop_nameForm(ModelForm):
    class Meta:
        model = Group_name
        fields = ('name', 'description', 'course', 'fk_discipline')


class DistributionForm(ModelForm):
    class Meta:
        model = Distribution
        fields = ('fk_discipline', 'fk_employee', 'fk_group_name')

class HomeworkForm(ModelForm):
    class Meta:
        model = Homework
        fields = ('title', 'description','presence', 'file', 'date_of_deliviri', 'appointment_date', 'fk_employee', 'fk_group')
        widgets = {
            'date_of_deliviri': DateInput,
            'appointment_date': DateInput,
        }


class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ('fk_student', 'fk_discipline', 'date_of_visit', 'presence')
        widgets = {
            'date_of_visit': DateInput,
        }

class Homework_checkForm(ModelForm):
    class Meta:
        model = Homework_check
        fields = ('assessment', 'fk_employee' , 'fk_homework', 'fk_student')
        widgets = {
            'fk_employee':  forms.HiddenInput(attrs={'class':'form-control'})
        }

class DisciplineForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Discipline
        fields = ('name', 'description', 'captcha',)


class DiaryForm(ModelForm):
    class Meta:
        model = Diary
        fields = ('fk_student', 'fk_discipline', 'fk_homework_check',)

class CreateUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2',]


class ContactForm(forms.Form):

    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class':'form-control', "rows": 5}))
    content = forms.CharField(label='Текст', widget=forms.TextInput(attrs={'class':'form-control', "rows": 5}))

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ('title', 'post','image', 'date',)
        widgets = {
            'date': DateInput,
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
