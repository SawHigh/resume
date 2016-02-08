# _*_ coding:utf-8 _*_

from django.conf.urls import patterns, url, include
from django.contrib import admin
from .views import log_in, ProjectList, ProjectCreate, ProjectUpdate, ProjectDelete, ProjectBrowse, \
ProfileList, ProfileUpdate, ProfileBrowse, AvatarUpdate,\
ContactList, ContactCreate, ContactUpdate, ContactDelete, ContactBrowse, \
SkillList, SkillCreate, SkilltUpdate, SkillDelete, SkillBrowse, \
EducationList, EducationCreate, EducationUpdate, EducationDelete, EducationBrowse, \
WorkLogList, WorkLogCreate, WorkLogUpdate, WorkLogDelete, WorkLogBrowse, \
UserList

urlpatterns = patterns('',
    
    url(r'^login/$', log_in, name='login'),
    
    url(r'^api/user/$', UserList.as_view()),
    
    url(r'^api/project/(?P<pk>\d+)/$', ProjectBrowse.as_view()),  #pk:用户id
    url(r'^api/project/list/$', ProjectList.as_view()),
    url(r'^api/project/create/$', ProjectCreate.as_view()),
    url(r'^api/project/(?P<pk>\d+)/update/$', ProjectUpdate.as_view()), #pk:对象id
    url(r'^api/project/(?P<pk>\d+)/delete/$', ProjectDelete.as_view()), #pk:对象id
    
    url(r'^api/profile/(?P<pk>\d+)/$', ProfileBrowse.as_view()),
    url(r'^api/profile/list/$', ProfileList.as_view(), name="profile_list"),
    url(r'^api/profile/(?P<pk>\d+)/update/$', ProfileUpdate.as_view()),
    url(r'^api/profile/avatar/(?P<pk>\d+)/update/$', AvatarUpdate.as_view(), name="avatar_update"),
    
    url(r'^api/contact/(?P<pk>\d+)/$', ContactBrowse.as_view(), name="contact_browse"),
    url(r'^api/contact/list/$', ContactList.as_view(), name="contact_list"),
    url(r'^api/contact/create/$', ContactCreate.as_view(), name="contact_create"),
    url(r'^api/contact/(?P<pk>\d+)/update/$', ContactUpdate.as_view(), name="contact_update"),
    url(r'^api/contact/(?P<pk>\d+)/delete/$', ContactDelete.as_view(), name="contact_delete"),
    
    url(r'^api/skill/(?P<pk>\d+)/$', SkillBrowse.as_view()),
    url(r'^api/skill/list/$', SkillList.as_view()),
    url(r'^api/skill/create/$', SkillCreate.as_view()),
    url(r'^api/skill/(?P<pk>\d+)/update/$', SkilltUpdate.as_view()),
    url(r'^api/skill/(?P<pk>\d+)/delete/$', SkillDelete.as_view()),
    
    url(r'^api/education/(?P<pk>\d+)/$', EducationBrowse.as_view()),
    url(r'^api/education/list/$', EducationList.as_view()),
    url(r'^api/education/create/$', EducationCreate.as_view()),
    url(r'^api/education/(?P<pk>\d+)/update/$', EducationUpdate.as_view()),
    url(r'^api/education/(?P<pk>\d+)/delete/$', EducationDelete.as_view()),
    
    url(r'^api/worllog/(?P<pk>\d+)/$', WorkLogBrowse.as_view()),
    url(r'^api/worllog/list/$',WorkLogList.as_view()),
    url(r'^api/worllog/create/$', WorkLogCreate.as_view()),
    url(r'^api/worllog/(?P<pk>\d+)/update/$',WorkLogUpdate.as_view()),
    url(r'^api/worllog/(?P<pk>\d+)/delete/$', WorkLogDelete.as_view()),


    url(r'^admin/', include(admin.site.urls)),
)
