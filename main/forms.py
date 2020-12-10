from django.utils import timezone
from .models import Task, Zadtb
from django.forms import ModelForm, TextInput, DateInput

class FormZan(ModelForm):
    class Meta:
        model = Zadtb
        dat_v=timezone.now()

        fields = ["id", "dz", "zan", "tema", "dlit_z", "otm", "pro"]

        widgets = {
            "id": "id",
            "dat_vre": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'дата'

            }),
            "dz": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'задание N'

            }),
            "zan": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Урок N'

            }),
            "tema": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема'

            }),
            "dlit_z": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Длительность'

            }),
            "otm": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отметка'

            }),
            "pro": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Проведение'

            }),

        }

class TaskForm(ModelForm):
    class Meta:
        # pass

        model = Task
        #tasks = Task.objects.order_by('id')


        fields = [
             "name", "fname", "fname_R", "vozr",
            "gorod", "strana", "telefon", "Skyyyd",
            "viber", "stupen", "grupp", "uroven"
        ]

        widgets = {

            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'

            }),
            "fname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "fname_R": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО Родителей'
            }),
            "vozr":  TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'возрост'
            }),
            "gorod": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'город'
            }),
            "strana": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'страна'
            }),
            "telefon":  TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'телефон'
            }),
            "Skyyyd": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Skype'
            }),
            "viber": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'viber'
            }),
            "stupen": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ступень'
            }),
            "grupp": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'группа'
            }),
            "uroven": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'уровень'
            })
        }
