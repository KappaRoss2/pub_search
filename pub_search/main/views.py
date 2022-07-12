from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework.viewsets import ModelViewSet

from .parser import springer as sp, elsiever as els, elibrary as elib
import concurrent.futures as pool
from .parser import init_parser as ip
from .models import Scimag
from .parser import find_preprint as fp
from .parser import find_copy as fc
from .forms import TabForm
import time
from .forms import UserRegistrationForm, LoginRegistrationForm
from .tasks import find_preprint_async as fpa
from .tasks import find_copy_async as fca


def home(request):
    return render(request, 'main/home.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'user_form': user_form})


def login(request):
    user_form = LoginRegistrationForm()
    return render(request, 'registration/login.html', {'user_form': user_form})


def get_article(request):
    if request.method == "POST":
        article = request.POST.get('article')
        articles = Scimag.objects.filter(title__contains=f'{article}')

    doi = [x.doi for x in articles]

    with pool.ThreadPoolExecutor(max_workers=30) as executer:
        preprint = executer.map(fpa, doi)
        copy = executer.map(fca, doi)

    result = zip(articles, preprint, copy)

    return render(request, 'main/home.html', {'result': result})


def add_article(request):
    print(request.POST['user'])
    error = ''
    if request.method == 'POST':
        form = TabForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверной'
            print(error)
    form = TabForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/home.html', data)


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')






