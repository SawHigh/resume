from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sawhighA.views.home', name='home'),
    url(r'^backend/$', 'sawhighA.views.backend_home', name='backend_home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^sawhigh/', include('resume.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
