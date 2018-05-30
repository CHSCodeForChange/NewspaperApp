from django.conf.urls import url
from django.contrib.auth.models import User

from . import views

urlpatterns = [
    url(r'^$', views.viewPapers, name='viewPapers'),
    url(r'^(?P<paper_id>[0-9]+)/$', views.viewPaper, name='viewPaper'),

    url(r'^createPaper/', views.createPaper, name='createPaper'),
    url(r'^editPaper/(?P<paper_id>[0-9]+)/', views.editPaper, name='editPaper'),

    url(r'^addSection/', views.addSection, name='addSection'),
    url(r'^editSection/(?P<section_id>[0-9]+)/', views.editSection, name='editSection'),
]
