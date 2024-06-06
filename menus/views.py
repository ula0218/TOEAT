from django.views.generic import CreateView
from .forms import MenuForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Menu


class CategorySelectionView(LoginRequiredMixin, CreateView):
    template_name = 'menus/select.html'
    form_class = MenuForm
    success_url = reverse_lazy('users:home')

    def form_valid(self, form):
        user_id = self.request.user.id
        form.instance.user_id = user_id
        return super().form_valid(form)