from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from resume.models import Profile

def home(request):
    return render(request, "home.html")

@login_required(login_url=reverse_lazy("login"))
def backend_home(request):
    user=request.user
    if not Profile.objects.filter(user=user).exists():
        i = Profile.objects.create(user=user)
        i.save()
    return render(request, "backend_home.html")