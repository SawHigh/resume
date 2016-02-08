from django.shortcuts import render
from .models import Project, Profile, Contact, Skill, Education, WorkLog
from django.contrib.auth.models import User
from .forms import LoginForm
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from utils.base_views import WebListApiView
from utils.mixins import CommonApiMixin, ImageResizeMixin
from utils.apiviews import ManagerListView, ManagerCreatView,ManagerUpdateView, ManagerDeleteView, CommonListView
from .forms import AvatarForm

def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data["username"]
            pw = form.cleaned_data["password"]
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(request, user)
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
    
class ProjectCreate(ManagerCreatView):
    model = Project
    field_names = [
                  "title",
                  "condition",
                  "description",
                  "published_date",
                  "link",
                  "source_code",
                  ]
    
class ProjectUpdate(ManagerUpdateView):
    model = Project 

class AvatarUpdate(ImageResizeMixin, ManagerUpdateView):
    model = Project
    form = AvatarForm
    image_field = "avatar"
    max_size = 200

class ProjectDelete(ManagerDeleteView):
    model = Project 
    
class ProfileList(ManagerListView):
    model = Profile

class ProfileUpdate(ManagerUpdateView):
    model = Profile
    
class ContactList(ManagerListView):
    model = Contact
    
class ContactCreate(ManagerCreatView):
    model = Contact
    field_names = [
                  "name",
                  "link",
                  ]
    
class ContactUpdate(ManagerUpdateView):
    model = Contact

class ContactDelete(ManagerDeleteView):
    model = Contact
        
class SkillList(ManagerListView):
    model = Skill
    
class SkillCreate(ManagerCreatView):
    model = Skill
    field_names = [
                  "name",
                  "degree",
                  ]
    
class SkilltUpdate(ManagerUpdateView):
    model = Skill

class SkillDelete(ManagerDeleteView):
    model = Skill
    
class EducationList(ManagerListView):
    model = Education
    
class EducationCreate(ManagerCreatView):
    model = Education
    field_names = [
                  "start",
                  "end",
                  "title",
                  ]
    
class EducationUpdate(ManagerUpdateView):
    model = Education

class EducationDelete(ManagerDeleteView):
    model = Education

class WorkLogList(ManagerListView):
    model = WorkLog
    
class WorkLogCreate(ManagerCreatView):
    model = WorkLog
    field_names = [
                  "start",
                  "end",
                  "company",
                  "job",
                  ]
    
class WorkLogUpdate(ManagerUpdateView):
    model = WorkLog

class WorkLogDelete(ManagerDeleteView):
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