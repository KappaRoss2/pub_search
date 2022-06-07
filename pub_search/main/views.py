from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse
from .parser import springer as sp, elsiever as els, elibrary as elib






def home(request):
    return render(request, 'main/home.html')

def get_article(request):
    if request.method == "POST":
        article = request.POST.get('article')
        url_springer = f'https://link.springer.com/search?query={article}&facet-content-type=%22Article%22'
        url_elsiever = f'https://www.sciencedirect.com/search?qs={article}'
        url_elibrary_part = article

        springer = sp.springer(url_springer)
        elsiever = els.elsiever(url_elsiever)
        elibrary = elib.elibrary(url_elibrary_part)

        springer.run('springer.csv')
        elsiever.run('elsiever.csv')
        elibrary.run('elibrary.csv')

        results = [springer.result, elsiever.result, elibrary.result]
        return render(request, 'main/home.html', {'title': 'Результаты поиска', 'results': results})


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')




