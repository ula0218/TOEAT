from django.views.generic import CreateView
from .forms import MenuForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Menu
from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView


class CategorySelectionView(LoginRequiredMixin, CreateView):
    template_name = 'menus/select.html'
    form_class = MenuForm
    success_url = reverse_lazy('users:home')

    def form_valid(self, form):
        user_id = self.request.user.id
        form.instance.user_id = user_id
        return super().form_valid(form)
    
class MapView(View):
    def get(self, request):
        google_api_key = settings.GOOGLE_MAPS_API_KEY
        return render(request, "menus/maps.html", {"google_api_key": google_api_key})
