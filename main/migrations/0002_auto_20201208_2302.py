# Generated by Django 3.1.3 on 2020-12-08 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date_d',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task',
        ),
        migrations.RemoveField(
            model_name='task',
            name='title',
        ),
        migrations.AddField(
            model_name='task',
            name='Skyyyd',
            field=models.CharField(default=0, max_length=30, verbose_name='Skype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='fname',
            field=models.CharField(default=1, max_length=30, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='fname_R',
            field=models.CharField(default='FFFFF', max_length=30, verbose_name='Родитель'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='gorod',
            field=models.CharField(default='Минск', max_length=30, verbose_name='город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='grupp',
            field=models.CharField(default='1', max_length=30, verbose_name='группа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='Иван', max_length=30, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='strana',
            field=models.CharField(default='Беларусь', max_length=30, verbose_name='страна'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='stupen',
            field=models.CharField(default='1', max_length=30, verbose_name='ступень'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='telefon',
            field=models.IntegerField(default='375296767676', verbose_name='телефон'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='uroven',
            field=models.CharField(default='1', max_length=30, verbose_name='уровень'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='viber',
            field=models.CharField(default='1', max_length=30, verbose_name='viber'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='vozr',
            field=models.IntegerField(default='1', verbose_name='возрост'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Zadtb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zan', models.IntegerField(verbose_name='Занятие')),
                ('dlit_z', models.IntegerField(verbose_name='Длительность')),
                ('dat_vre', models.DateTimeField(max_length=4, verbose_name='ДатаВремя')),
                ('tema', models.CharField(max_length=30, verbose_name='тема')),
                ('dz', models.CharField(max_length=30, verbose_name='домашее задание')),
                ('otm', models.IntegerField(verbose_name='отметка')),
                ('pro', models.BooleanField(verbose_name='проведение')),
                ('tzzz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.task')),
            ],
        ),
    ]
