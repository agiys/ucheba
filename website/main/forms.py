from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput





class MilitaryForm(ModelForm):
    class Meta:
        model = Military
        fields = {'number','dislocation','type_troops','companies' }

        widgets= {
            'number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'номер'
            }),
            'dislocation': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'дислокация',
            }),
            'type_troops': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вид войск',
            }),
            'companies': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Рота',
            }),
        }

class Type_troopsForm(ModelForm):
    class Meta:
        model = Type_troop
        fields = {'title' }

        widgets= {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'названи'

            }),
        }

class CompaniesForm(ModelForm):
    class Meta:
        model = Companies
        fields = {'title','number_employees' }

        widgets= {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название'
            }),
            'number_employees': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Личный состав',
            }),

        }

class EmployeesForm(ModelForm):
    class Meta:
        model = Employees
        fields = {'fist_name','companies','post','year_birth','year_enlistment','length_service','honors','military_activies' }

        widgets= {
            'fist_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            'companies': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Рота',
            }),
            'post': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность',
            }),
            'year_enlistment': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата поступления',
            }),
            'length_service': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Выслуга',
            }),
            'honors': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Награды',
            }),
            'military_activies': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Активность',
            }),
            'year_birth': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год рождения',
            }),
        }


class DislocationForm(ModelForm):
    class Meta:
        model = Dislocatio
        fields = {'country','city','address','squar' }

        widgets= {
            'country': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страна'
            }),
            'city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город',
            }),
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адресс',
            }),
            'squar': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Площадь',
            }),
        }