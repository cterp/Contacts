from django.conf.urls import patterns, include, url
from django.contrib import admin
import contactbook.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', contactbook.views.ListContact.as_view(),
        name='contacts-list',),
    url(r'^new$', contactbook.views.CreateContact.as_view(),
        name='contacts-new',),
    url(r'^edit/(?P<pk>\d+)/$', contactbook.views.UpdateContact.as_view(),
        name='contacts-edit',),
    url(r'^delete/(?P<pk>\d+)/$', contactbook.views.DeleteContact.as_view(),
        name='contacts-delete',),
)

urlpatterns += staticfiles_urlpatterns()
