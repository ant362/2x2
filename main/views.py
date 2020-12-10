from django.shortcuts import render, redirect
from django.views.generic import DeleteView, UpdateView, CreateView
from .models import Task, Zadtb
from .forms import TaskForm, FormZan
from django.utils import timezone
from django.views.generic.list import ListView

def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, "main/index.html", {"title": "Главная страница сайта", "tasks": tasks})


def about(request):
    return render(request, "main/about.html")
def rasp(request):
    return render(request, "main/rasp.html")
def domz(request):
    return render(request, "main/domz.html")

def spis(request):
    tasks = Task.objects.order_by('id')
    return render(request, "main/spis.html", {"name": tasks, "tasks": tasks})

def trenaz(request):
    #return render(request, "main/tren0.html")
    return render(request, "main/trenaz.html")


def creat(request):
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spis')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {

        'form': form,
        'error': error
    }

    return render(request, "main/creat.html", context)


def creat2(request):
    error = ""

    if request.method == 'POST':
        form = FormZan(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spis')
        else:
            error = 'Форма была неверной'
    form = FormZan()
    context = {

        'form': form,
        'error': error,
        'tzzz': pk
    }

    return render(request, "main/cr_list.html", context)
# изменение данных в бд



# удаление данных из бд
class Delete(DeleteView):
    model = Task
    success_url = "/spis"
    template_name = "main/delete.html"


class Edit(UpdateView):
    model = Task
    success_url = "/spis"
    template_name = "main/edit.html"
    form_class = TaskForm

class Cr_list(CreateView):
    model = Zadtb
    success_url = "/spis"
    queryset = Zadtb.objects.all()
    template_name = "main/cr_list.html"
    form_class = FormZan

    def form_valid(self, form):
            new_record = form.save(commit=False)
            new_record.tzzz_id = self.kwargs['pk']  # нужен pk
            new_record.save()
            form.save()
            return redirect("/spis")

#    def get_success_url(self):
#        return reverse('piece-detail', kwargs={'pk': self.kwargs['pk']})


class Ed_list(UpdateView):
    model = Zadtb
    #queryset = Zadtb.objects.order_by('id')
    success_url = "/spis"
    template_name = "main/ed_list.html"
    form_class = FormZan

class List(UpdateView):

    model = Task
    success_url = "/spis"
    template_name = "main/list.html"
    form_class = TaskForm


