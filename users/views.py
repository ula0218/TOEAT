from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView,CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.list import ListView
from django.shortcuts import redirect
from .models import User
from .forms import CustomUserForm

class UserHomeView(TemplateView):
    template_name = 'users/home.html'
    
class UserRegisterView(FormView):
    template_name = 'users/register.html'
    success_url = reverse_lazy("todos:create") 

    def form_valid(self, form):
        form.save()
        return redirect(self.get_success_url())
    
class UserLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("users:home")

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")

class UserDataCreateView(CreateView):
    model = User
    form_class = CustomUserForm
    template_name = 'users/data.html' 
    success_url = reverse_lazy('todos:create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        for user in users:
            user.bmi = calculate_bmi(user.height, user.weight)
        context['users'] = users
        return context
    
def calculate_bmi(height, weight):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return bmi
    