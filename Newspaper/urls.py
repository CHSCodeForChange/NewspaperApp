from django.conf.urls import url
from django.contrib.auth.models import User

from . import views

urlpatterns = [
    url(r'^$', views.viewPapers, name='viewPapers'),
    url(r'^(?P<paper_id>[0-9]+)/$', views.viewPaper, name='viewPaper'),

    url(r'^create', views.createPaper, name='createPaper'),
    url(r'^(?P<paper_id>[0-9]+)/edit', views.editPaper, name='editPaper'),
    url(r'^(?P<paper_id>[0-9]+)/delete', views.deletePaper, name='deletePaper'),

    url(r'^(?P<paper_id>[0-9]+)/section/add', views.addSection, name='addSection'),
    url(r'^section/(?P<section_id>[0-9]+)/edit', views.editSection, name='editSection'),
    url(r'^section/(?P<section_id>[0-9]+)/delete', views.deleteSection, name='deleteSection'),
]
