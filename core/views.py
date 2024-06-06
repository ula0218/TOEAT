from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse_lazy

class UserTemplateView(TemplateView):
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('users:home'))
        return super().dispatch(request, *args, **kwargs)