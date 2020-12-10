from django.db import models
from datetime import datetime

#date = models.DateField(blank=False, default=datetime.now().strftime("%d.%m.%Y"))
'''
Имя          name
Фамилия      fname
Фамилия Р    fname_R
возрост      vozr
город        gorod
страна       strana
телефон      telefon
Skype        Skype
viber        viber
ступень      stupen
группа       grupp
уровень      uroven
'''

class Task(models.Model):
    name    = models.CharField('Имя',max_length=30)
    fname   = models.CharField('Фамилия',max_length=30)
    fname_R = models.CharField('Родитель',max_length=30)
    vozr    = models.IntegerField('возрост')
    gorod   = models.CharField('город',max_length=30)
    strana  = models.CharField('страна',max_length=30)
    telefon = models.IntegerField('телефон')
    Skyyyd = models.CharField('Skype',max_length=30)
    viber   = models.CharField('viber',max_length=30)
    stupen  = models.CharField('ступень',max_length=30)
    grupp   = models.CharField('группа',max_length=30)
    uroven  = models.CharField('уровень',max_length=30)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Zadtb(models.Model):
    tzzz = models.ForeignKey(Task, on_delete=models.CASCADE)
    zan = models.IntegerField('Занятие')
    dlit_z = models.IntegerField('Длительность')
    dat_vre = models.DateTimeField('ДатаВремя', max_length=4)
    tema = models.CharField('тема', max_length=30)
    dz = models.CharField('домашее задание', max_length=30)
    otm = models.IntegerField('отметка')
    pro = models.BooleanField('проведение')


    #def get_absolute_url(self):
    #    return reverse("articles:zadtb-detali",kwargs={"id":self.id})
    def __str__(self):
        return self.dz

