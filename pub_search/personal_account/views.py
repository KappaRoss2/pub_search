from django.shortcuts import render
from django.contrib.auth.models import User
from main.models import Tab
from django.http import HttpResponse

# Create your views here.


def get_tabs(request):
    tabs = ''
    if request.method == "GET":
        tabs = Tab.objects.filter(user=request.user)

    for el in tabs:
        print(el.preprint)
    return render(request, 'personal_account/personal_account.html', {'tabs': tabs})