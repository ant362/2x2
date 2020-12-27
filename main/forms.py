import datetime
import sys
from django.conf.urls import  url
from django.shortcuts import render
from .models import Task, Zadtb
from django.forms import ModelForm, TextInput, DateTimeInput





class FormZan_Cr(ModelForm):
    class Meta:
        model = Zadtb

        fields = [ "dat_vre", "dz", "zan", "tema", "dlit_z", "otm", "pro" ]

        widgets = {
            "id": "id",
            'gpp':'gpp',
            "dat_vre": DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',



            }),
            "dz": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Задание"

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

class FormZan_Ed(ModelForm):
    class Meta:
        model = Zadtb


        fields = [ "dat_vre", "dz", "zan", "tema", "dlit_z", "otm", "pro" ]

        widgets = {
            "id": "id",
            'gpp':'gpp',
            "dat_vre": DateTimeInput(attrs={
                'class': 'form-control',
                'type': "",
            }),
            "dz": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Задание"

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
             "dtz", "name", "fname", "fname_R", "vozr",
            "gorod", "strana", "telefon", "Skyyyd",
            "viber", "stupen", "grupp", "uroven"
        ]

        widgets = {

            "name": TextInput(attrs={
                'width': '60px',


            }),
            "dtz": DateTimeInput(attrs={
                'class': 'form-control',
                'type': "",
            }),
            "fname": TextInput(attrs={
                'width': '60px',
            }),
            "fname_R": TextInput(attrs={
                'width': '60px',
            }),
            "vozr":  TextInput(attrs={
                'width': '60px',
            }),
            "gorod": TextInput(attrs={
                'width': '60px',
            }),
            "strana": TextInput(attrs={
                'width': '60px',
            }),
            "telefon":  TextInput(attrs={
                'width': '60px',
            }),
            "Skyyyd": TextInput(attrs={
                'width': '60px',
            }),
            "viber": TextInput(attrs={
                'width': '60px',
            }),
            "stupen": TextInput(attrs={
                'width': '60px',
            }),
            "grupp": TextInput(attrs={
                'width': '60px',
            }),
            "uroven": TextInput(attrs={
                'width': '60px',
            })
        }


