from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.contrib.admin import widgets



class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'surname', 'middle_name', 'date_of_birth', 'course', 'number', 'group',)


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'name', 'surname', 'middle_name', 'date_of_birth', 'description', 'image', 'fk_position', 'fk_accses',)
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
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
        fields = ('name', 'description',)



class HomeworkForm(ModelForm):
    class Meta:
        model = Homework
        fields = ('title', 'description', 'date_of_deliviri', 'appointment_date')


class Homework_checkForm(ModelForm):
    class Meta:
        model = Homework_check
        fields = ('assessment', 'fk_employee', 'fk_homework', 'fk_student')

class InformationForm(ModelForm):
    class Meta:
        model = Information
        fields = ('title', 'description', 'image',)


class DisciplineForm(ModelForm):
    class Meta:
        model = Discipline
        fields = ('name', 'description',)



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class':'form-control', "rows": 5}))
    content = forms.CharField(label='Текст', widget=forms.TextInput(attrs={'class':'form-control', "rows": 5}))