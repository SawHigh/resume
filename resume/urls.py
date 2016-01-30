from django.conf.urls import patterns, url, include
from django.contrib import admin
from .views import resume_list, resume_create, resume_update, resume_delete, log_in, ResumeApi

urlpatterns = patterns('',
    # Examples:
    url(r'^$', resume_list, name='resume_list'),
    url(r'^resume_create/$', resume_create, name='resume_create'),
    url(r'^resume_update/(?P<pk>\d+)/$', resume_update, name='resume_update'),
    url(r'^resume_delete/(?P<pk>\d+)/$', resume_delete, name='resume_delete'),
    
    url(r'^login/$', log_in, name='login'),
    
    url(r'^api/$', ResumeApi.as_view(), name='api'),
    

    url(r'^admin/', include(admin.site.urls)),
)
