from django.shortcuts import render, get_object_or_404
from .models import Resume
from .forms import ResumeForm, LoginForm
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import login, authenticate

@login_required(login_url=reverse_lazy("login"))
def resume_list(request):
    list1 = Resume.objects.all().order_by("-published_date")
    context = {"list":list1}
    return render(request, "resume_list.html", context)
    
@login_required(login_url=reverse_lazy("login"))
def resume_create(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('resume_list'))
    else:
        form = ResumeForm()
    context = {"form":form}
    return render(request, "resume_create.html", context)    

@login_required(login_url=reverse_lazy("login"))
def resume_update(request, pk):
    instance = get_object_or_404(Resume, pk=pk)
    if request.method == "POST":
        form = ResumeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('resume_list'))
    else:
        form = ResumeForm(instance=instance)
    context = {"form":form}
    return render(request, "resume_create.html", context)  

@login_required(login_url=reverse_lazy("login"))
@require_POST
def resume_delete(request, pk):
    instance = get_object_or_404(Resume, pk=pk)
    instance.delete()
    return HttpResponseRedirect(reverse('resume_list'))

def resume_show(request):
    list1 = Resume.objects.all()
    context = {"list":list1}
    return render(request, "resume_list.html", context)

def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data["username"]
            pw = form.cleaned_data["password"]
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("resume_list"))
            else:
                return HttpResponseRedirect(reverse("login"))
    else:
        form = LoginForm()
    context = {"form":form}
    return render(request, "resume_create.html", context)  
# Create your views here.
