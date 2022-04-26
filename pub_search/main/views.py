from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView



def home(request):
    return render(request, 'main/home.html')




class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')




