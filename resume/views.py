from django.shortcuts import render
from .models import Project, Profile, Contact, Skill, Education
from django.contrib.auth.models import User
from .forms import LoginForm
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from utils.apiviews import WebListApiView, CommonApiMixin, ManagerApiMixin, WebCreateApiView,\
WebUpdateApiView, WebDeleteApiView, QueryFromUrlMixin

def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data["username"]
            pw = form.cleaned_data["password"]
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(request, user)
                if not user.profile:
                    Profile.objects.create(user=user)
                    Profile.save()
                return HttpResponseRedirect(reverse("project_list"))
            else:
                return HttpResponseRedirect(reverse("login"))
    else:
        form = LoginForm()
    context = {"form":form}
    return render(request, "project_create.html", context)  

class UserList(CommonApiMixin, WebListApiView):    
    models = User
    fields = [
              "id",
              "username"
              ]

class ProjectList(ManagerApiMixin, WebListApiView):
    model = Project
    def query(self, request):
        return {"user":request.user}
    
class ProjectCreate(ManagerApiMixin,WebCreateApiView):
    model = Project
    field_names = [
                  "title",
                  "condition",
                  "description",
                  "published_date",
                  "link",
                  "source_code",
                  ]
    
    def extend_data(self, request):
        return {"user":request.user}
    
class ProjectUpdate(ManagerApiMixin,WebUpdateApiView):
    model = Project 

class ProjectDelete(ManagerApiMixin,WebDeleteApiView):
    model = Project 
    
class ProfileList(ManagerApiMixin, WebListApiView):
    model = Project
    def query(self, request):
        return {"user":request.user}

class ProfileUpdate(ManagerApiMixin,WebUpdateApiView):
    model = Profile
    
class ContactList(ManagerApiMixin, WebListApiView):
    model = Contact
    def query(self, request):
        return {"user":request.user}
    
class ContactCreate(ManagerApiMixin,WebCreateApiView):
    model = Contact
    field_names = [
                  "name",
                  "link",
                  ]
    
    def extend_data(self, request):
        return {"user":request.user}
    
class ContactUpdate(ManagerApiMixin,WebUpdateApiView):
    model = Contact

class ContactDelete(ManagerApiMixin,WebDeleteApiView):
    model = Contact
    
    
class SkillList(ManagerApiMixin, WebListApiView):
    model = Skill
    def query(self, request):
        return {"user":request.user}
    
class SkillCreate(ManagerApiMixin,WebCreateApiView):
    model = Skill
    field_names = [
                  "name",
                  "degree",
                  ]
    
    def extend_data(self, request):
        return {"user":request.user}
    
class SkilltUpdate(ManagerApiMixin,WebUpdateApiView):
    model = Skill

class SkillDelete(ManagerApiMixin,WebDeleteApiView):
    model = Skill
    
class EducationList(ManagerApiMixin, WebListApiView):
    model = Education
    def query(self, request):
        return {"user":request.user}
    
class EducationCreate(ManagerApiMixin,WebCreateApiView):
    model = Education
    field_names = [
                  "start",
                  "end",
                  "title",
                  ]
    
    def extend_data(self, request):
        return {"user":request.user}
    
class EducationUpdate(ManagerApiMixin,WebUpdateApiView):
    model = Education

class EducationDelete(ManagerApiMixin,WebDeleteApiView):
    model = Education
    
    
class ProjectBrowse(CommonApiMixin, QueryFromUrlMixin, WebListApiView):
    model = Project
 
class ProfileBrowse(CommonApiMixin, QueryFromUrlMixin, WebListApiView):
    model = Profile 
    
class ContactBrowse(CommonApiMixin, QueryFromUrlMixin, WebListApiView):
    model = Contact
    
class SkillBrowse(CommonApiMixin, QueryFromUrlMixin, WebListApiView):
    model = Skill

class EducationBrowse(CommonApiMixin, QueryFromUrlMixin, WebListApiView):
    model = Education    
