# views.py

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
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("events:view")

class TodoListView(ListView):
    model = Todo
    template_name = 'todos/index.html'
    context_object_name = 'todos' 

    def get_queryset(self):
        user = self.request.user
        queryset = Todo.objects.filter(user=user)
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
        return context
