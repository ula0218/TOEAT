from datetime import datetime
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm
import plotly.graph_objs as go
from django.db.models import Count
from django.db.models.functions import TruncDate
from plotly.io import to_json


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

class TodoStatsView(TemplateView):
    template_name = 'todos/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 日期
        date_counts = Todo.objects.annotate(date_annotated=TruncDate('date')).values('date_annotated').annotate(total=Count('id')).order_by('date_annotated')
        dates = [item['date_annotated'].strftime('%Y/%m/%d') for item in date_counts]
        date_totals = [item['total'] for item in date_counts]

        # 每日飲食內容紀錄
        date_details = {}
        for item in date_counts:
            date_str = item['date_annotated'].strftime('%Y/%m/%d')
            records = Todo.objects.filter(date=item['date_annotated'])
            date_details[date_str] = [{'food': record.food, 'type': dict(Todo.TYPES_CHOICES)[record.type],'hungry': dict(Todo.HUNGRY_CHOICES)[record.hungry]} for record in records]

        # 圖表對象
        date_chart = go.Bar(
            y=dates,
            x=date_totals,
            orientation='h',
            name='日期',
            marker=dict(color='rgb(255, 192, 203)', line=dict(color='rgb(255, 105, 180)', width=1.5)),
            customdata=[date_details[date] for date in dates],
            hovertemplate='%{y}<br>次數: %{x}<extra></extra>'
        )       

        # 圖表佈局
        layout = go.Layout(
            xaxis={'title': '單日用餐次數'},
            yaxis={'title': '日期'},
            width=800,
            height=600,
            plot_bgcolor='rgb(230, 230, 250)',
        )

        fig = go.Figure(data=[date_chart], layout=layout)

        # 圖表轉換成 JSON 
        chart_json = to_json(fig)

        context['chart_json'] = chart_json
        return context