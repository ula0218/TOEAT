# views.py
from datetime import datetime
from django.http import JsonResponse
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todos/create.html"
    success_url = reverse_lazy("users:home")


    def form_valid(self, form):
        user_id = self.request.user.id
        form.instance.user_id = user_id
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("events:view")

class TodoListView(ListView):
    model = Todo
    template_name = 'todos/index.html'
    context_object_name = 'todos'

    def get_queryset(self):
        user = self.request.user
        start_date = self.request.GET.get('startDate')
        end_date = self.request.GET.get('endDate')

        queryset = Todo.objects.filter(user=user)
        if start_date and end_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            queryset = queryset.filter(date__range=(start_date, end_date))
        else:
            queryset = Todo.objects.none() #沒填日期範圍時，返回空的

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todos = context['todos']
        grouped_todos = {}
        for todo in todos:
            date = todo.date.strftime('%Y-%m-%d')
            if date not in grouped_todos:
                grouped_todos[date] = []
            grouped_todos[date].append(todo)
        context['grouped_todos'] = grouped_todos
        context['filter_applied'] = self.request.GET.get('startDate') and self.request.GET.get('endDate')
        return context
