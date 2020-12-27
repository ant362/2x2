from django.shortcuts import render, redirect
from django.views.generic import DeleteView, UpdateView, CreateView
from .models import Task, Zadtb
from .forms import TaskForm, FormZan_Cr, FormZan_Ed

from django.contrib.auth.decorators import login_required
from calendar import HTMLCalendar
from datetime import datetime

#from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe

# def calendar(request, year, month):
#   my_workouts = Workouts.objects.order_by('my_date').filter(
#     my_date__year=year, my_date__month=month
#   )
#   cal = WorkoutCalendar(my_workouts).formatmonth(year, month)
#   return render_to_response('my_template.html', {'calendar': mark_safe(cal),})




def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, "main/index.html", {"title": "Главная страница сайта", "tasks": tasks})


def about(request):
    return render(request, "main/about.html")



@login_required
def domz(request):
    return render(request, "main/domz.html")

@login_required
def spis(request):
    tasks = Task.objects.order_by('id')
    return render(request, "main/spis.html", {"name": tasks, "tasks": tasks})

@login_required
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



#календарь
class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(dtz__day=day)
        d = ''

        for event in events_per_day:
            d += f'<li width=200px> {event.name} ** {event.dtz.strftime ("%H:%M")} </li>'

        if day != 0:
            return f"<td width=200px ><span  class='date'>{day}</span><ul width=200px> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr  > {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        events = Task.objects.filter(dtz__year=self.year, dtz__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal

@login_required

def rasp(request):
    cal = Calendar(datetime.today().year, datetime.today().month)
    html_out = cal.formatmonth(withyear=True)
    return render(request, "main/rasp.html", {"html_out": mark_safe(html_out), })

# @login_required
# def rasp(request):
#     c = calendar.HTMLCalendar()
#     html_out = c.formatmonth(datetime.today().year, datetime.today().month)
#     return render(request, "main/rasp.html", {"html_out": mark_safe(html_out), })

# class CalendarView(LoginRequiredMixin, generic.ListView):
#     login_url = 'signup'
#     model = Event
#     template_name = 'calendar.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         d = get_date(self.request.GET.get('month', None))
#         cal = Calendar(d.year, d.month)
#         html_cal = cal.formatmonth(withyear=True)
#         context['calendar'] = mark_safe(html_cal)
#         context['prev_month'] = prev_month(d)
#         context['next_month'] = next_month(d)
#         return context




# удаление данных из бд
class Delete(DeleteView):
    model = Task
    success_url = "/spis"
    template_name = "main/delete.html"

# удаление данных из бд
class Del_list(DeleteView):
    model = Zadtb
    success_url = "/spis"
    template_name = "main/del_list.html"
    def get_success_url(self, *args, **kwargs):
        redirect_to = self.request.GET.get('next')
        return redirect_to

class Edit(UpdateView):
    model = Task
    success_url = "/spis"
    template_name = "main/edit.html"
    form_class = TaskForm

class Cr_list(CreateView):

    model = Zadtb

    #success_url = "/spis"
    queryset = Zadtb.objects.all()
    template_name = "main/cr_list.html"

    form_class = FormZan_Cr

    def form_valid(self, form, *args, **kwargs):
            new_record = form.save(commit=False)
            new_record.tzzz_id = self.kwargs['pk']  # нужен pk
            new_record.save()
            form.save()
            return redirect(self.request.GET.get('next'))    # СРАБОТАЛО



#    def get_success_url(self):
#        return reverse('piece-detail', kwargs={'pk': self.kwargs['pk']})


class Ed_list(UpdateView):
    model = Zadtb
    queryset = Zadtb.objects.order_by('id')

    success_url = "/spis"
    template_name = "main/ed_list.html"
    form_class = FormZan_Ed

    #def get_success_url(self):
    #    return redirect('zad','pk')

    def get_success_url(self, *args, **kwargs):
        redirect_to = self.request.GET.get('next')
        return redirect_to


class List(UpdateView):

    model = Task
    success_url = "/spis"
    template_name = "main/list.html"
    form_class = TaskForm


