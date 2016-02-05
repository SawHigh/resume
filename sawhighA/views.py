from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy

def home(request):
    return render(request, "home.html")

@login_required(login_url=reverse_lazy("login"))
def backend_home(request):
    return render(request, "backend_home.html")