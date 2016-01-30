from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'resume.views.resume_show', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^sawhigh/', include('resume.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
