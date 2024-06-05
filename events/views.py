from django.views.generic import TemplateView
from todos.models import Todo
from django.urls import reverse_lazy

class CalendarView(TemplateView):
    template_name = 'calendars/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        todos = Todo.objects.filter(user=self.request.user)

        context['todos'] = todos
        return context