from django.shortcuts import render
from .models import Project, Profile, Contact, Skill, Education, WorkLog
from django.contrib.auth.models import User
from .forms import LoginForm
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from utils.apiviews import WebListApiView, CommonApiMixin, ManagerApiMixin, WebCreateApiView,\
WebUpdateApiView, WebDeleteApiView, OwnerPassMixin, ManagerListView, CommonListView

def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data["username"]
            pw = form.cleaned_data["password"]
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(request, user)
                if not Profile.objects.filter(user=user).exists():
                    i = Profile.objects.create(user=user)
                    i.save()
                return HttpResponseRedirect(reverse("backend_home"))
            else:
                return HttpResponseRedirect(reverse("login"))
    else:
        form = LoginForm()
    context = {"form":form}
    return render(request, "project_create.html", context)  

class UserList(CommonApiMixin, WebListApiView):    
    model = User
    fields = [
              "id",
              "username"
              ]

class ProjectList(ManagerListView):
    model = Project
    
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
    
class ProjectUpdate(OwnerPassMixin,WebUpdateApiView):
    model = Project 

class ProjectDelete(OwnerPassMixin,WebDeleteApiView):
    model = Project 
    
class ProfileList(ManagerListView):
    model = Project

class ProfileUpdate(OwnerPassMixin,WebUpdateApiView):
    model = Profile
    
class ContactList(ManagerListView):
    model = Contact
    
class ContactCreate(ManagerApiMixin,WebCreateApiView):
    model = Contact
    field_names = [
                  "name",
                  "link",
                  ]
    
    def extend_data(self, request):
        return {"user":request.user}
    
class ContactUpdate(OwnerPassMixin,WebUpdateApiView):
    model = Contact

class ContactDelete(OwnerPassMixin,WebDeleteApiView):
    model = Contact
        
class SkillList(ManagerListView):
    model = Skill
    
class SkillCreate(ManagerApiMixin,WebCreateApiView):
    model = Skill
    field_names = [
                  "name",
                  "degree",
                  ]
    
    def extend_data(self, request):
        return {"user":request.user}
    
class SkilltUpdate(OwnerPassMixin,WebUpdateApiView):
    model = Skill

class SkillDelete(OwnerPassMixin,WebDeleteApiView):
    model = Skill
    
class EducationList(ManagerListView):
    model = Education
    
class EducationCreate(ManagerApiMixin,WebCreateApiView):
    model = Education
    field_names = [
                  "start",
                  "end",
                  "title",
                  ]
    
    def extend_data(self, request):
        return {"user":request.user}
    
class EducationUpdate(OwnerPassMixin,WebUpdateApiView):
    model = Education

class EducationDelete(OwnerPassMixin,WebDeleteApiView):
    model = Education

class WorkLogList(ManagerListView):
    model = WorkLog
    
class WorkLogCreate(ManagerApiMixin,WebCreateApiView):
    model = WorkLog
    field_names = [
                  "start",
                  "end",
                  "company",
                  "job",
                  ]
    
    def extend_data(self, request):
        return {"user":request.user}
    
class WorkLogUpdate(OwnerPassMixin,WebUpdateApiView):
    model = WorkLog

class WorkLogDelete(OwnerPassMixin,WebDeleteApiView):
    model = WorkLog
    
class ProjectBrowse(CommonListView):
    model = Project
 
class ProfileBrowse(CommonListView):
    model = Profile 
    
class ContactBrowse(CommonListView):
    model = Contact
    
class SkillBrowse(CommonListView):
    model = Skill

class EducationBrowse(CommonListView):
    model = Education    

class WorkLogBrowse(CommonListView):
    model = WorkLog