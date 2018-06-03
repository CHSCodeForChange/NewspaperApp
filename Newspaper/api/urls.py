from django.conf.urls import url
from django.contrib.auth.models import User

from .views import *

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', GetPaper.as_view(), name='viewPaper'),
    url(r'^$', ListPapers.as_view(), name='listPapers'),
    url('^section/$', ListSections.as_view(), name='listSections'),
]
