from django.shortcuts import render
from .models import Project, Profile, UserContact, Skill, Education, WorkLog, Contact
from django.contrib.auth.models import User
from .forms import LoginForm
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from utils.base_views import WebListApiView
from utils.mixins import CommonApiMixin, ImageResizeMixin
from utils.apiviews import ManagerListView, ManagerCreatView,ManagerUpdateView, ManagerDeleteView, CommonListView, \
MustLoginCreateView, MustLoginListView
from resume.forms import ContactForm, AvatarForm

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
              ["profile", "id"],
              ["profile", "name"]
              ]

class ContactList(MustLoginListView):
    model = Contact
    fields = ["id", "name", "icon"]
    
class ContactCreate(ImageResizeMixin, MustLoginCreateView):
    model = Contact
    form = ContactForm
    image_field = "icon"
    max_width = 200
    max_height = 200
    
    field_names = ['name', 'icon']
    
    def get_form(self, request):
        return self.form(request.POST, request.FILES)

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
    model = Profile
    form = AvatarForm
    image_field = "avatar"
    max_width = 200
    max_height = 200

class ProjectDelete(ManagerDeleteView):
    model = Project 
    
class ProfileList(ManagerListView):
    model = Profile

class ProfileUpdate(ManagerUpdateView):
    model = Profile
    
class UserContactList(ManagerListView):
    model = UserContact
    
class UserContactCreate(ManagerCreatView):
    model = UserContact
    field_names = [
                  "contact_id",
                  "link",
                  ]
    
class UserContactUpdate(ManagerUpdateView):
    model = UserContact

class UserContactDelete(ManagerDeleteView):
    model = UserContact
        
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
    
class UserContactBrowse(CommonListView):
    model = UserContact
    
class SkillBrowse(CommonListView):
    model = Skill

class EducationBrowse(CommonListView):
    model = Education    

class WorkLogBrowse(CommonListView):
    model = WorkLog