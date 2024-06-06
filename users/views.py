from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Record
from django.contrib.auth import login
from .forms import CustomUserForm,CustomLoginForm,CustomUserCreationForm


class UserHomeView(TemplateView):
    template_name = 'users/home.html'
    
class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("todos:create") 

    def form_valid(self, form):
        response = super().form_valid(form)
    
        user = form.save()
        login(self.request, user)
        
        return response
    
class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = CustomLoginForm

    def get_success_url(self):
        return reverse_lazy("users:home")

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")

class UserDataCreateView(CreateView):
    model = Record
    form_class = CustomUserForm
    template_name = 'users/data.html' 
    success_url = reverse_lazy('todos:create')

    def form_valid(self, form):
        user_id = self.request.user.id
        form.instance.user_id = user_id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = Record.objects.filter(user_id=self.request.user.id)
        context['users'] = users
        for user in users:
            user.bmi = calculate_bmi(user.height, user.weight)
        return context
    
def calculate_bmi(height, weight):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return bmi
    