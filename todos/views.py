# views.py

from django.views.generic.edit import CreateView
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

